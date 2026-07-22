from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.ticket import close_ticket, create_ticket, get_ticket, list_tickets, put_ticket
from app.dependencies import get_db
from app.schemas.ticket import TicketCreate, TicketPut, TicketRead


router = APIRouter()


@router.post("/", response_model=TicketRead, status_code=status.HTTP_201_CREATED)
def create_ticket_endpoint(payload: TicketCreate, db: Session = Depends(get_db)) -> TicketRead:
    return create_ticket(db, payload)


@router.get("/", response_model=list[TicketRead])
def list_tickets_endpoint(db: Session = Depends(get_db)) -> list[TicketRead]:
    return list_tickets(db)


@router.put("/{ticket_id}", response_model=TicketRead)
def put_ticket_endpoint(
    ticket_id: int, payload: TicketPut, db: Session = Depends(get_db)
) -> TicketRead:
    ticket = get_ticket(db, ticket_id)
    if ticket is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    return put_ticket(db, ticket, payload)


@router.patch("/{ticket_id}/close", response_model=TicketRead)
def close_ticket_endpoint(ticket_id: int, db: Session = Depends(get_db)) -> TicketRead:
    ticket = get_ticket(db, ticket_id)
    if ticket is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    return close_ticket(db, ticket)
