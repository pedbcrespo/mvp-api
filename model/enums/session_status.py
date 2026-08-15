
from enum import StrEnum

class SessionStatus(StrEnum):
    SCHEDULED = 'SCHEDULED'
    DONE = 'DONE'
    MISSED = 'MISSED'
    RESCHEDULED = 'RESCHEDULED'
    CANCELLED = 'CANCELLED'