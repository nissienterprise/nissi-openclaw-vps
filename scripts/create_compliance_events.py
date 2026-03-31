#!/usr/bin/env python3
"""Create annual compliance/tax deadline events in Nissi Tech Oficial Calendar."""

from datetime import datetime, timezone
from google_calendar import create_event

ATTENDEES = ["mmrodriguez1987@gmail.com", "vguido1983@gmail.com"]
REMINDERS = [10080, 4320, 1440]  # 1 week, 3 days, 1 day (in minutes)
RECURRENCE = ["RRULE:FREQ=YEARLY"]

EVENTS = [
    {
        "summary": "Annual Report – Sunbiz (Florida)",
        "start": datetime(2026, 5, 1, tzinfo=timezone.utc),
        "end":   datetime(2026, 5, 1, tzinfo=timezone.utc),
        "description": (
            "DEADLINE: Annual Report filing with the State of Florida (Sunbiz).\n\n"
            "This is a mandatory yearly renewal to keep the company active and in good standing. "
            "Filing must be completed at sunbiz.org before May 1st to avoid a $400 late fee.\n\n"
            "Steps:\n"
            "1. Go to sunbiz.org → File Annual Report\n"
            "2. Enter the company document number\n"
            "3. Verify/update registered agent and officer information\n"
            "4. Pay the filing fee ($138.75 for profit corporations)\n"
            "5. Save confirmation receipt\n\n"
            "⚠️ Late filing after May 1st incurs a $400 penalty."
        ),
    },
    {
        "summary": "IRS Tax Return Deadline – C Corporation (Form 1120)",
        "start": datetime(2026, 4, 15, tzinfo=timezone.utc),
        "end":   datetime(2026, 4, 15, tzinfo=timezone.utc),
        "description": (
            "DEADLINE: Federal income tax return for C Corporations (IRS Form 1120).\n\n"
            "This is the annual federal tax filing deadline for C-Corp entities. "
            "The return covers the previous fiscal year's income, deductions, and tax liability.\n\n"
            "Steps:\n"
            "1. Gather all financial statements (P&L, Balance Sheet) for the fiscal year\n"
            "2. Work with your CPA to prepare Form 1120\n"
            "3. File electronically via IRS e-file or mail to the appropriate IRS center\n"
            "4. Pay any tax owed to avoid interest and penalties\n\n"
            "💡 If you need more time, file Form 7004 before this date to request an automatic "
            "6-month extension (new deadline: October 15).\n\n"
            "⚠️ An extension to file is NOT an extension to pay. Estimate and pay any tax due by April 15."
        ),
    },
    {
        "summary": "IRS Extended Tax Return Deadline – C Corporation (Form 1120)",
        "start": datetime(2026, 10, 15, tzinfo=timezone.utc),
        "end":   datetime(2026, 10, 15, tzinfo=timezone.utc),
        "description": (
            "EXTENDED DEADLINE: Federal income tax return for C Corporations (Form 1120) – "
            "6-month automatic extension.\n\n"
            "This deadline applies only if Form 7004 was filed by April 15 to request an extension. "
            "No further extensions are available after this date.\n\n"
            "Steps:\n"
            "1. Confirm Form 7004 was accepted by the IRS\n"
            "2. Finalize and review Form 1120 with your CPA\n"
            "3. File the completed return before October 15\n"
            "4. Verify any balance due was already paid by April 15 to minimize interest\n\n"
            "⚠️ This is the absolute final deadline for C-Corp federal tax returns. "
            "No additional extensions are permitted."
        ),
    },
]


def main():
    print("=== Creating Annual Compliance Events ===\n")
    for ev in EVENTS:
        print(f"Creating: {ev['summary']} ({ev['start'].strftime('%B %d')})...")
        result = create_event(
            summary=ev["summary"],
            start=ev["start"],
            end=ev["end"],
            description=ev["description"],
            recurrence=RECURRENCE,
            reminder_minutes=REMINDERS,
            all_day=True,
        )
        print(f"  ✓ Created — ID: {result.get('id')}")
        print(f"  Link: {result.get('htmlLink')}\n")

    print("All events created successfully.")


if __name__ == "__main__":
    main()
