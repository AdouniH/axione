from sqlalchemy.orm import Session

from app.models.ticket import Ticket, TicketStatus
from app.schemas.ticket import TicketCreate, TicketPut


def create_ticket(db: Session, payload: TicketCreate) -> Ticket:
    ticket = Ticket(**payload.model_dump())
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def get_ticket(db: Session, ticket_id: int) -> Ticket | None:
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


def list_tickets(db: Session) -> list[Ticket]:
    return db.query(Ticket).all()


def put_ticket(db: Session, ticket: Ticket, payload: TicketPut) -> Ticket:
    ticket.title = payload.title
    ticket.description = payload.description
    ticket.status = payload.status
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def close_ticket(db: Session, ticket: Ticket) -> Ticket:
    ticket.status = TicketStatus.CLOSED
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket
