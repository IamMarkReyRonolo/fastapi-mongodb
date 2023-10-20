from server.models.question import Activity


async def record_activity(question, activity_title: str = None, staff_involved: str = None, staff_uuid: str = None, update_note: str = None):
    activity = None

    if activity_title == 'Delete':
        question_type = question["question_type"]
        activity = Activity(title=activity_title,
                            details=f'{activity_title}d a {question_type} question.',
                            staff_involved=staff_involved,
                            question_id= str(question['id']),
                            staff_id= staff_uuid)
    else:
        details = ""
        if(activity_title == 'Approved'):
            if(update_note):
                details = update_note
            else:
                details = f"Approved a {question.question_type} question."
        elif(activity_title == 'Pending'):
            details = f"Moved to pending status."
        elif(activity_title == 'Create'):
            details = f"Created a {question.question_type} question."
        else:
            details = update_note
        activity = Activity(title=activity_title, 
                            details=details,
                            staff_involved=staff_involved,
                            question_id= str(question.id),
                            staff_id= staff_uuid
                            )
        
    # save activity to db
    await activity.insert()
