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

async def typing_action(chat_id: int, context: CallbackContext, response_text: str) -> None: #add typng indicatore to ther chat for human like feel
    read_pause =random.uniform(0.5, 1.0) #rndom delay for typing
    await asyncio.sleep(read_pause) #wait for the delay
    await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING) #typing action
    chars = len(response_text) #get the length of the response text
    typing_time = min(chars * 0.022 + random.uniform(02, 0.6), 4.0) #calculate the typing time based on the length of the text
    await asyncio.sleep(typing_time) #wait for the typing time