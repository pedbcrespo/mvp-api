
from enum import Enum

class SessionStatus(Enum):
    SCHEDULED = 'SCHEDULED'
    DONE = 'DONE'
    MISSED = 'MISSED'
    RESCHEDULED = 'RESCHEDULED'
    CANCELLED = 'CANCELLED'