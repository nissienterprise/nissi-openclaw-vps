#!/usr/bin/env python3
"""Google Calendar integration via Service Account for OpenClaw / Nissi Technology."""

import os
from datetime import datetime, timezone, timedelta
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build

# --- Config ---
SCOPES = ["https://www.googleapis.com/auth/calendar"]

SERVICE_ACCOUNT_INFO = {
    "type": "service_account",
    "project_id": "nissiproject",
    "private_key_id": "378e405e85fc9d86d771709cd45e726e97f58194",
    "private_key": (
        "-----BEGIN PRIVATE KEY-----\n"
        "MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDAb7mP7uzKfxep\n"
        "nxhQJn7TuPpaFVS4saPutfK7Y3Xi4ZkFa6Xf3zm+YeRFiMo4tBPdTIt3vI8OjpdF\n"
        "BZkRopHEeIYv/88byVaqD5MdhQCH3+FIR4G2aDhcs78OkNRl9q4qt2q3m3TVSjKc\n"
        "olyLt/e9EOJoM95edcqW9K5Mo5bEB0dw7BLkQFm9+vUtr3xb6ZQi/PRqdc/tSdnq\n"
        "tcueY0EZa+6uUlo2Sdz1sQvZCW0HYk9zREsBvm5Ix8Y6xKh62SQpnnzDyEYwbRis\n"
        "USfC5Psl+oe1ywIMvGrJ0M1du0GB5yASMhlXVzdCQDcnS6y2yzEYMfEltbiJ40zA\n"
        "SNaAiZrlAgMBAAECgf8Ty2pLDp33i8XjV3ooxHecpRUbhGuH6WieJW59LWidmJck\n"
        "95htxDMsYjrDlvk2MU/ZyQXk9dXBVD7l2q2OzX+GYN9suzjn+CNHWv1xtpICErAZ\n"
        "v0FDLMqfaTM99v03f9MVPHNob5U/sLeED9of2ndL+3Cj8gdDBYV8Aa9BiDz57O0Z\n"
        "yhwB+4zJxJsmw5W0taPR1Fbbrohu0CclsqTpcCVFLaGIkRTQCYQ2g3wTGWry3xsn\n"
        "8ScHkaL2+gPdDah/j5H5xdREHJk0TxBK+YrXT1dZ67SjIfB5rF0ftkRd1JI/x8Sh\n"
        "zamV2SKdNbYPvwpLDoU0HRYqzmbrxad1HcBTJEECgYEA+iQU5E2CGWmYUWR4puPm\n"
        "5JMYFIOWKk407viBubiQ+x/VKh/nSrCo50MikVXEJBhyHcRvY2fOesVasqfD3B0A\n"
        "6bFGoOrC03o1EdiI0CpXWyuo8zKPKvbGbDHN68hOKq5adb5sI8+DJj1rrS/uVamg\n"
        "j/eYZ7tNqeTWeCqLmPMKJ5ECgYEAxPGhSnvsrX6pVswY/kSKqmrtDRDLpIHLLCRD\n"
        "DzYIzavovaMt/t82EG42rx+eeRMDGrtThqmbs/8Vx1s/xwD7NUEpJgB7bGYbf1uC\n"
        "pyiSVX/fnAzodnE4XopQF+i7d0TKEUFBedpbpNQb6Is4tKSHLS3hP2T3lig32NWK\n"
        "mnsYnBUCgYEAu5hfyrCOR3y37SLKkW8N9JKUVp4w+l1YuXfJ4n0Wzh8bgNIYZh2D\n"
        "Lp1cyV5nESL8QnLVjtmFMvHbiWzkKKnfy2NWMsydfHiEYHPidyuqBAgEVw+t62zT\n"
        "dsULSC8a4EuOMAu1kk3Ib99UZ7gwqDHk5tOrivAf2LB0X/6YXwa2sOECgYBxa7L3\n"
        "AX2hwVNm8G3oabLuSFwy7RxKppFK36tbJERXpoyIQmTn5sbtGXwWyP/sPH3KNF37\n"
        "LMzGEb8KK8wEINWLqvY2s4phOEDXzOzmtd/oq5cs+OYb6EKNd9x+mIL2QkCZRVqf\n"
        "AZlLyPg1qZBDwIk1BLo3Vz+bU5guIXUMWJ4orQKBgQC5g8aSZRbDbfieb1zNal5K\n"
        "gbAcoDQ7T67pUuoCSY71i/+cO9GOcJra6NmhGWn/pfS/LWvoQlsY0GvqO5+LR9Fa\n"
        "Lus0HMZXco9yl03L57kGkGdHmDr32MfWr6iosI2Mvj/nm00uWn4qygnC1EJIwoE+\n"
        "kWsQnev8+c1mkLgJt1yI3A==\n"
        "-----END PRIVATE KEY-----\n"
    ),
    "client_email": "openclaw@nissiproject.iam.gserviceaccount.com",
    "client_id": "101384389170202145718",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/openclaw%40nissiproject.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com",
}

# Primary calendar (nissienterprise.ai@gmail.com = "Nissi Tech Oficial Calendar")
DEFAULT_CALENDAR_ID = "nissienterprise.ai@gmail.com"


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _get_service():
    credentials = service_account.Credentials.from_service_account_info(
        SERVICE_ACCOUNT_INFO, scopes=SCOPES
    )
    return build("calendar", "v3", credentials=credentials)


def _ensure_calendar_in_list(service, calendar_id):
    """Add a shared calendar to the service account's list if not already there."""
    calendars = service.calendarList().list().execute()
    ids = [c["id"] for c in calendars.get("items", [])]
    if calendar_id not in ids:
        service.calendarList().insert(body={"id": calendar_id}).execute()


def _fmt(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%S") + "Z"


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def create_event(
    summary: str,
    start: datetime,
    end: datetime,
    description: str = "",
    location: str = "",
    calendar_id: str = DEFAULT_CALENDAR_ID,
    recurrence: list = None,
    reminder_minutes: list = None,
    attendees: list = None,
    all_day: bool = False,
) -> dict:
    """Create a calendar event. Returns the created event dict.

    Args:
        recurrence:       e.g. ["RRULE:FREQ=YEARLY"]
        reminder_minutes: e.g. [10080, 4320, 1440]  (1 week, 3 days, 1 day)
        attendees:        list of email strings
        all_day:          if True, uses date-only format (start/end time ignored)
    """
    service = _get_service()
    _ensure_calendar_in_list(service, calendar_id)

    if all_day:
        body = {
            "summary": summary,
            "description": description,
            "location": location,
            "start": {"date": start.strftime("%Y-%m-%d")},
            "end": {"date": end.strftime("%Y-%m-%d")},
        }
    else:
        body = {
            "summary": summary,
            "description": description,
            "location": location,
            "start": {"dateTime": _fmt(start), "timeZone": "UTC"},
            "end": {"dateTime": _fmt(end), "timeZone": "UTC"},
        }

    if recurrence:
        body["recurrence"] = recurrence

    if reminder_minutes:
        body["reminders"] = {
            "useDefault": False,
            "overrides": [{"method": "email", "minutes": m} for m in reminder_minutes],
        }

    if attendees:
        body["attendees"] = [{"email": e} for e in attendees]

    return service.events().insert(calendarId=calendar_id, body=body).execute()


def list_events(
    max_results: int = 10,
    time_min: datetime = None,
    calendar_id: str = DEFAULT_CALENDAR_ID,
) -> list:
    """Return upcoming events from the calendar."""
    service = _get_service()
    _ensure_calendar_in_list(service, calendar_id)

    if time_min is None:
        time_min = datetime.now(timezone.utc)

    result = service.events().list(
        calendarId=calendar_id,
        timeMin=_fmt(time_min),
        maxResults=max_results,
        singleEvents=True,
        orderBy="startTime",
    ).execute()
    return result.get("items", [])


def update_event(
    event_id: str,
    summary: str = None,
    start: datetime = None,
    end: datetime = None,
    description: str = None,
    location: str = None,
    calendar_id: str = DEFAULT_CALENDAR_ID,
) -> dict:
    """Patch an existing event. Only provided fields are updated."""
    service = _get_service()
    _ensure_calendar_in_list(service, calendar_id)

    patch = {}
    if summary is not None:
        patch["summary"] = summary
    if description is not None:
        patch["description"] = description
    if location is not None:
        patch["location"] = location
    if start is not None:
        patch["start"] = {"dateTime": _fmt(start), "timeZone": "UTC"}
    if end is not None:
        patch["end"] = {"dateTime": _fmt(end), "timeZone": "UTC"}

    return service.events().patch(
        calendarId=calendar_id, eventId=event_id, body=patch
    ).execute()


def delete_event(event_id: str, calendar_id: str = DEFAULT_CALENDAR_ID) -> None:
    """Delete an event by ID."""
    service = _get_service()
    _ensure_calendar_in_list(service, calendar_id)
    service.events().delete(calendarId=calendar_id, eventId=event_id).execute()


def list_calendars() -> list:
    """Return all calendars visible to the service account."""
    service = _get_service()
    result = service.calendarList().list().execute()
    return result.get("items", [])


# ---------------------------------------------------------------------------
# CLI quick-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== Google Calendar - OpenClaw ===\n")

    print("Calendarios disponibles:")
    for cal in list_calendars():
        print(f"  - {cal.get('summary')} ({cal['id']})")

    print("\nCreando evento de prueba...")
    now = datetime.now(timezone.utc)
    event = create_event(
        summary="Evento de Prueba - OpenClaw",
        start=now + timedelta(hours=1),
        end=now + timedelta(hours=2),
        description="Creado automáticamente por el script de integración de OpenClaw.",
    )
    print(f"  ✓ Evento creado: {event.get('summary')}")
    print(f"  ID:   {event.get('id')}")
    print(f"  Link: {event.get('htmlLink')}")
