#!/usr/bin/env python3
"""Fetch a small summary from the Google Analytics 4 Data API and write it to
JSON for the /stats/ page. Runs at deploy time in CI.

Requires:
  - env GA_PROPERTY_ID        numeric GA4 property id (e.g. 123456789)
  - env GOOGLE_APPLICATION_CREDENTIALS  path to a service-account JSON key
  - pip package: google-analytics-data

Writes to $OUT (default: _site/assets/analytics.json). On any error it exits
non-zero WITHOUT writing, so the committed seed file is kept and the page
simply stays on its "coming soon" state.
"""
import json
import os
import sys
from datetime import datetime, timezone

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    OrderBy,
    RunReportRequest,
)

PROPERTY_ID = os.environ["GA_PROPERTY_ID"]
OUT = os.environ.get("OUT", "_site/assets/analytics.json")
LAST_30 = [DateRange(start_date="30daysAgo", end_date="today")]

client = BetaAnalyticsDataClient()


def run(dimensions, metrics, order_bys=None, limit=None):
    req = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[Dimension(name=d) for d in dimensions],
        metrics=[Metric(name=m) for m in metrics],
        date_ranges=LAST_30,
        order_bys=order_bys or [],
        limit=limit,
    )
    return client.run_report(req)


def as_int(v):
    return int(float(v))


def main():
    # Headline totals
    t = run([], ["activeUsers", "sessions", "screenPageViews", "averageSessionDuration"])
    m = t.rows[0].metric_values
    active, sessions, views = as_int(m[0].value), as_int(m[1].value), as_int(m[2].value)
    avg_seconds = round(float(m[3].value))

    # Daily active users (trend)
    d = run(
        ["date"],
        ["activeUsers"],
        order_bys=[OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name="date"))],
    )
    series = [
        {"date": r.dimension_values[0].value, "users": as_int(r.metric_values[0].value)}
        for r in d.rows
    ]

    # Top pages by views
    p = run(
        ["pagePath"],
        ["screenPageViews"],
        order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="screenPageViews"), desc=True)],
        limit=5,
    )
    top_pages = [
        {"path": r.dimension_values[0].value, "views": as_int(r.metric_values[0].value)}
        for r in p.rows
    ]

    # Device category split
    dev = run(["deviceCategory"], ["sessions"])
    devices = [
        {"cat": r.dimension_values[0].value, "sessions": as_int(r.metric_values[0].value)}
        for r in dev.rows
    ]

    out = {
        "sample": False,
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "range_days": 30,
        "active_users": active,
        "sessions": sessions,
        "views": views,
        "avg_engagement_seconds": avg_seconds,
        "series": series,
        "top_pages": top_pages,
        "devices": devices,
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {OUT}: {active} users, {sessions} sessions, {views} views over 30 days")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # keep the seed on any failure
        print(f"GA fetch failed: {e}", file=sys.stderr)
        sys.exit(1)
