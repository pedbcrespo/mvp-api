from enum import Enum

class ProcedureStatus(Enum):
    ACTIVE = 'ACTIVE'
    INTERRUPTED = 'INTERRUPTED'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'