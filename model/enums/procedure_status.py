from enum import StrEnum

class ProcedureStatus(StrEnum):
    ACTIVE = 'ACTIVE'
    INTERRUPTED = 'INTERRUPTED'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'