async def record_user_snapshot(user):
    snapshot = {
        "user_id": user.id, #save user id to database
        "first_name": user.first_name or "", #save name
        "last_name": user.last_name or "",
        "username": (user.username or "").lower(), #save username to database
        "ts": datetime.now(timezone.utc), #timestamp for the changes
    }

    last = await_history_col.find_one(
        {"user_id": user.id},
        sort=[("ts", -1)],
    )

    if last:
        if (
            last.get("first_name") == snapshot["first_name"] #to prevent creating nreew entried incasr user already exists in the database
            and last.get("last_name") == snapshot["last_name"]
            and last.get("username") == snapshot["username"]
        ):
            return
        await history_col.insert_one(snapshot) #entry

