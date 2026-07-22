def test_create_ticket(client) -> None:
    response = client.post(
        "/api/v1/tickets/",
        json={
            "title": "Ticket A",
            "description": "Description A",
            "status": "open",
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["id"] > 0
    assert data["title"] == "Ticket A"
    assert data["status"] == "open"


def test_list_tickets(client) -> None:
    client.post(
        "/api/v1/tickets/",
        json={
            "title": "Ticket 1",
            "description": "Description 1",
            "status": "open",
        },
    )

    response = client.get("/api/v1/tickets/")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1


def test_get_ticket_by_id(client) -> None:
    created = client.post(
        "/api/v1/tickets/",
        json={
            "title": "Ticket unique",
            "description": "Description unique",
            "status": "open",
        },
    )
    ticket_id = created.json()["id"]

    response = client.get(f"/api/v1/tickets/{ticket_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == ticket_id


def test_get_unknown_ticket_returns_404(client) -> None:
    response = client.get("/api/v1/tickets/9999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Ticket not found"
