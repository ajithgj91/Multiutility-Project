def generate_email_body(subject):
    # Simple template-based generation
    templates = {
        "meeting": "Dear [Name],\n\nWe have scheduled a meeting regarding [Topic]. Please be available at [Time].\n\nBest regards,\n[Your Name]",
        "thank you": "Dear [Name],\n\nThank you for your assistance with [Task]. It was greatly appreciated.\n\nBest regards,\n[Your Name]",
        "follow up": "Dear [Name],\n\nI am following up on our previous conversation about [Topic]. Please let me know your thoughts.\n\nBest regards,\n[Your Name]",
        "Project Kickoff":"Dear Team, I am excited to announce the kickoff of our new project. We have a great opportunity ahead, and I look forward to working with all of you.Please review the attached project plan and prepare any questions you may have.The initial meeting is scheduled for [Date] at [Time]. Regards,[Your Name]",
        "Monthly Report":"Hi Everyone, Attached is the monthly report for our department. Please review the document and provide any feedback by [Date].We will discuss this report in our meeting on [Date] at [Time].Best,[Your Name]",
        "meeting": "Dear [Name],\n\nWe have scheduled a meeting regarding [Topic]. Please be available at [Time].\n\nBest regards,\n[Your Name]",
        "project_update": "Dear [Name],\n\nHere is the latest update on [Project]. Please review and let us know your thoughts.\n\nBest regards,\n[Your Name]",

        "performance_review": "Dear [Name],\n\nYour performance review for this period is ready. We will discuss your performance and future goals during our meeting on [Time].\n\nBest regards,\n[Your Name]",

        "monthly_report": "Dear [Name],\n\nAttached is the monthly report for our department. Please review the document and provide any feedback by [Time].\n\nBest regards,\n[Your Name]",

        "meeting_agenda": "Dear [Name],\n\nPlease find the agenda for our upcoming meeting attached. We will cover the following topics: [Topic 1], [Topic 2], and [Topic 3]. The meeting will take place on [Time].\n\nBest regards,\n[Your Name]",

        "team_building_event": "Dear [Name],\n\nWe have scheduled a team-building event to strengthen our collaboration. The event will be held on [Time]. Please check the attached document for more details.\n\nLooking forward to your participation,\n[Your Name]",

        "project_deadline": "Dear [Name],\n\nJust a reminder that the deadline for the project is approaching on [Time]. Ensure all tasks are completed and submit your final reports by then.\n\nThank you,\n[Your Name]",

        "client_feedback": "Dear [Client Name],\n\nThank you for your feedback on our recent project. We have reviewed your comments and will address them during our next meeting on [Time].\n\nBest regards,\n[Your Name]",

        "policy_update": "Dear [Name],\n\nWe have updated our company policies. Please review the attached document to stay informed about the changes. The new policies will take effect from [Time].\n\nBest regards,\n[Your Name]",

        "training_session": "Dear [Name],\n\nWe are organizing a training session on [Topic] on [Time]. Please review the attached materials before the session.\n\nSee you there,\n[Your Name]",

        "financial_report": "Dear [Name],\n\nAttached is the quarterly financial report for your review. We will discuss the details during our meeting on [Time].\n\nBest regards,\n[Your Name]",

        "holiday_notice": "Dear [Name],\n\nPlease note that our office will be closed for the holiday season from [Start Date] to [End Date]. Ensure all urgent tasks are completed before the break.\n\nHappy Holidays,\n[Your Name]",

        "system_maintenance": "Dear [Name],\n\nWe will perform system maintenance on [Time]. Please save your work and log off before the scheduled maintenance.\n\nThank you for your cooperation,\n[Your Name]",

        "job_opening": "Dear [Name],\n\nWe have a new job opening for the position of [Job Title]. Please find the job description attached. Applications are due by [Time].\n\nBest regards,\n[Your Name]",

        "welcome_aboard": "Dear [New Employee Name],\n\nWelcome to the team! Attached are some documents to help you get started. We will have an orientation session on [Time].\n\nLooking forward to working with you,\n[Your Name]",

        "product_launch": "Dear [Name],\n\nWe are excited to announce the launch of our new product on [Time]. Please review the attached marketing materials and prepare for the launch event.\n\nBest regards,\n[Your Name]",

        "expense_report": "Dear [Name],\n\nPlease submit your expense report by [Time]. We will review the reports and address any issues during our meeting on [Time].\n\nThank you,\n[Your Name]",

        "vendor_contract": "Dear [Vendor Name],\n\nAttached is the contract for our upcoming project. We need your confirmation by [Time].\n\nLooking forward to your response,\n[Your Name]",

        "research_findings": "Dear [Name],\n\nAttached are the findings from our recent research. We will review the results during our meeting on [Time].\n\nBest regards,\n[Your Name]",

        "feedback_request": "Dear [Name],\n\nWe would appreciate your feedback on our recent presentation. Please send your comments by [Time].\n\nThank you,\n[Your Name]",

        "safety_training": "Dear [Name],\n\nWe have scheduled a safety training session on [Time]. Please review the attached training materials before the session.\n\nBest regards,\n[Your Name]",

        "project_update": "Dear [Name],\n\nHere is the latest update on the [Project] project. Please review and let us know your thoughts.\n\nBest regards,\n[Your Name]",

        "performance_review": "Dear [Name],\n\nYour performance review for this period is ready. We will discuss your performance and future goals during our meeting on [Time].\n\nBest regards,\n[Your Name]",

        "monthly_report": "Dear [Name],\n\nAttached is the monthly report for our department. Please review the document and provide any feedback by [Time].\n\nBest regards,\n[Your Name]",

        "meeting_agenda": "Dear [Name],\n\nPlease find the agenda for our upcoming meeting attached. We will cover the following topics: [Topic 1], [Topic 2], and [Topic 3]. The meeting will take place on [Time].\n\nBest regards,\n[Your Name]",

        "team_building_event": "Dear [Name],\n\nWe have scheduled a team-building event to strengthen our collaboration. The event will be held on [Time]. Please check the attached document for more details.\n\nLooking forward to your participation,\n[Your Name]",

        "project_deadline": "Dear [Name],\n\nJust a reminder that the deadline for the [Project] project is approaching on [Time]. Ensure all tasks are completed and submit your final reports by then.\n\nThank you,\n[Your Name]",

        "client_feedback": "Dear [Client Name],\n\nThank you for your feedback on our recent project. We have reviewed your comments and will address them during our next meeting on [Time].\n\nBest regards,\n[Your Name]",

        "policy_update": "Dear [Name],\n\nWe have updated our company policies. Please review the attached document to stay informed about the changes. The new policies will take effect from [Time].\n\nBest regards,\n[Your Name]",

        "training_session": "Dear [Name],\n\nWe are organizing a training session on [Topic] on [Time]. Please review the attached materials before the session.\n\nSee you there,\n[Your Name]",

        "financial_report": "Dear [Name],\n\nAttached is the quarterly financial report for your review. We will discuss the details during our meeting on [Time].\n\nBest regards,\n[Your Name]",

        "holiday_notice": "Dear [Name],\n\nPlease note that our office will be closed for the holiday season from [Start Date] to [End Date]. Ensure all urgent tasks are completed before the break.\n\nHappy Holidays,\n[Your Name]",

        "system_maintenance": "Dear [Name],\n\nWe will perform system maintenance on [Time]. Please save your work and log off before the scheduled maintenance.\n\nThank you for your cooperation,\n[Your Name]",

        "job_opening": "Dear [Name],\n\nWe have a new job opening for the position of [Job Title]. Please find the job description attached. Applications are due by [Time].\n\nBest regards,\n[Your Name]",

        "welcome_aboard": "Dear [New Employee Name],\n\nWelcome to the team! Attached are some documents to help you get started. We will have an orientation session on [Time].\n\nLooking forward to working with you,\n[Your Name]",

        "product_launch": "Dear [Name],\n\nWe are excited to announce the launch of our new product on [Time]. Please review the attached marketing materials and prepare for the launch event.\n\nBest regards,\n[Your Name]",

        "expense_report": "Dear [Name],\n\nPlease submit your expense report by [Time]. We will review the reports and address any issues during our meeting on [Time].\n\nThank you,\n[Your Name]",

        "vendor_contract": "Dear [Vendor Name],\n\nAttached is the contract for our upcoming project. We need your confirmation by [Time].\n\nLooking forward to your response,\n[Your Name]",

        "research_findings": "Dear [Name],\n\nAttached are the findings from our recent research. We will review the results during our meeting on [Time].\n\nBest regards,\n[Your Name]",

        "feedback_request": "Dear [Name],\n\nWe would appreciate your feedback on our recent presentation. Please send your comments by [Time].\n\nThank you,\n[Your Name]",

        "safety_training": "Dear [Name],\n\nWe have scheduled a safety training session on [Time]. Please review the attached training materials before the session.\n\nBest regards,\n[Your Name]",
        
        "illness_notice": "Dear [Name],\n\nI wanted to inform you that I am feeling unwell and will not be able to come to work today. I hope to recover soon and will keep you updated on my condition.\n\nThank you for understanding,\n[Your Name]",

        "resignation": "Dear [Manager's Name],\n\nI am writing to formally resign from my position at [Company] effective [Last Working Day]. I have enjoyed my time here and appreciate the opportunities I've been given.\n\nBest regards,\n[Your Name]",

        "party_invitation": "Hi [Name],\n\nYou're invited to a party at my place on [Date] at [Time]. We'll have lots of fun, food, and drinks. I hope you can make it!\n\nCheers,\n[Your Name]",

        "leave_request": "Dear [Manager's Name],\n\nI would like to request a leave of absence from [Start Date] to [End Date] due to [Reason]. Please let me know if this is approved.\n\nThank you,\n[Your Name]",

        "accident_report": "Dear [Manager's Name],\n\nI wanted to report that I had a minor accident on my way to work today. I am okay but will need some time to recover. I will keep you updated.\n\nBest regards,\n[Your Name]",

        "birthday_invitation": "Hi [Name],\n\nYou're invited to my birthday party on [Date] at [Time]. There will be cake, games, and lots of fun. I hope you can join us!\n\nBest,\n[Your Name]",

        "family_emergency": "Dear [Manager's Name],\n\nI am writing to inform you that I have a family emergency and will need to take some time off starting [Date]. I will keep you updated on my situation.\n\nThank you for understanding,\n[Your Name]",

        "thank_you_note": "Hi [Name],\n\nI wanted to say thank you for [Reason]. Your help and support mean a lot to me. I truly appreciate it.\n\nBest regards,\n[Your Name]",

        "congratulations": "Hi [Name],\n\nCongratulations on your [Achievement]! I am so happy for you and wish you all the best in your future endeavors.\n\nWarm regards,\n[Your Name]",

        "condolences": "Dear [Name],\n\nI was deeply saddened to hear about your loss. Please accept my heartfelt condolences and know that my thoughts are with you during this difficult time.\n\nSincerely,\n[Your Name]",

        "job_offer_acceptance": "Dear [Employer's Name],\n\nI am pleased to accept the job offer for the position of [Job Title] at [Company]. I am excited to join the team and contribute to the company's success.\n\nBest regards,\n[Your Name]",

        "farewell_message": "Hi [Name],\n\nAs you know, today is my last day at [Company]. I wanted to say goodbye and let you know how much I enjoyed working with you. Let's keep in touch!\n\nBest,\n[Your Name]",

        "get_well_soon": "Hi [Name],\n\nI heard that you're not feeling well. I hope you get better soon! Take care of yourself and let me know if you need anything.\n\nBest wishes,\n[Your Name]",

        "vacation_notice": "Dear [Manager's Name],\n\nI am writing to inform you that I will be on vacation from [Start Date] to [End Date]. I will ensure all my tasks are completed before I leave.\n\nThank you,\n[Your Name]",

        "wedding_invitation": "Hi [Name],\n\nI am thrilled to invite you to my wedding on [Date] at [Time]. Your presence would mean a lot to us. Please join us in celebrating this special day.\n\nBest regards,\n[Your Name]",

        "apology": "Dear [Name],\n\nI wanted to apologize for [Reason]. It was not my intention to [Cause/Action], and I am truly sorry for any inconvenience caused.\n\nSincerely,\n[Your Name]",

        "promotion_announcement": "Hi [Name],\n\nI am excited to share that I have been promoted to [New Position] at [Company]. Thank you for your support and encouragement.\n\nBest,\n[Your Name]",

        "maternity_leave": "Dear [Manager's Name],\n\nI am writing to inform you that I will be going on maternity leave starting [Date]. I plan to return on [Expected Return Date]. Please let me know if you need any additional information.\n\nThank you,\n[Your Name]",

        "retirement_announcement": "Dear [Name],\n\nI am writing to let you know that I will be retiring from my position at [Company] effective [Retirement Date]. I have enjoyed my time here and will cherish the memories.\n\nBest regards,\n[Your Name]",

        "congratulatory_note": "Hi [Name],\n\nI wanted to congratulate you on [Achievement]. Your hard work and dedication have truly paid off. Well done!\n\nBest wishes,\n[Your Name]",
      
        "illness_notice": "Dear [Manager's Name],\n\nI am writing to inform you that I am feeling unwell and will not be able to come to work today. I hope to recover soon and will keep you updated on my condition.\n\nThank you for understanding,\n[Your Name]",

        "resignation": "Dear [Manager's Name],\n\nI am writing to formally resign from my position at [Company] effective [Last Working Day]. I have enjoyed my time here and appreciate the opportunities I've been given.\n\nBest regards,\n[Your Name]",

        "party_invitation": "Hi [Name],\n\nYou are invited to a party at my place on [Date] at [Time]. We'll have lots of fun, food, and drinks. I hope you can make it!\n\nCheers,\n[Your Name]",

        "leave_request": "Dear [Manager's Name],\n\nI would like to request a leave of absence from [Start Date] to [End Date] due to [Reason]. Please let me know if this is approved.\n\nThank you,\n[Your Name]",

        "accident_report": "Dear [Manager's Name],\n\nI am writing to report that I had a minor accident on my way to work today. I am okay but will need some time to recover. I will keep you updated.\n\nBest regards,\n[Your Name]",

        "birthday_invitation": "Hi [Name],\n\nYou are invited to my birthday party on [Date] at [Time]. There will be cake, games, and lots of fun. I hope you can join us!\n\nBest,\n[Your Name]",

        "family_emergency": "Dear [Manager's Name],\n\nI am writing to inform you that I have a family emergency and will need to take some time off starting [Date]. I will keep you updated on my situation.\n\nThank you for understanding,\n[Your Name]",

        "thank_you_note": "Hi [Name],\n\nI wanted to say thank you for [Reason]. Your help and support mean a lot to me. I truly appreciate it.\n\nBest regards,\n[Your Name]",

        "congratulations": "Hi [Name],\n\nCongratulations on your [Achievement]! I am so happy for you and wish you all the best in your future endeavors.\n\nWarm regards,\n[Your Name]",

        "condolences": "Dear [Name],\n\nI was deeply saddened to hear about your loss. Please accept my heartfelt condolences and know that my thoughts are with you during this difficult time.\n\nSincerely,\n[Your Name]",

        "job_offer_acceptance": "Dear [Employer's Name],\n\nI am pleased to accept the job offer for the position of [Job Title] at [Company]. I am excited to join the team and contribute to the company's success.\n\nBest regards,\n[Your Name]",

        "farewell_message": "Hi [Name],\n\nAs you know, today is my last day at [Company]. I wanted to say goodbye and let you know how much I enjoyed working with you. Let's keep in touch!\n\nBest,\n[Your Name]",

        "get_well_soon": "Hi [Name],\n\nI heard that you're not feeling well. I hope you get better soon! Take care of yourself and let me know if you need anything.\n\nBest wishes,\n[Your Name]",

        "vacation_notice": "Dear [Manager's Name],\n\nI am writing to inform you that I will be on vacation from [Start Date] to [End Date]. I will ensure all my tasks are completed before I leave.\n\nThank you,\n[Your Name]",

        "wedding_invitation": "Hi [Name],\n\nI am thrilled to invite you to my wedding on [Date] at [Time]. Your presence would mean a lot to us. Please join us in celebrating this special day.\n\nBest regards,\n[Your Name]",

        "apology": "Dear [Name],\n\nI wanted to apologize for [Reason]. It was not my intention to [Cause/Action], and I am truly sorry for any inconvenience caused.\n\nSincerely,\n[Your Name]",

        "promotion_announcement": "Hi [Name],\n\nI am excited to share that I have been promoted to [New Position] at [Company]. Thank you for your support and encouragement.\n\nBest,\n[Your Name]",

        "maternity_leave": "Dear [Manager's Name],\n\nI am writing to inform you that I will be going on maternity leave starting [Date]. I plan to return on [Expected Return Date]. Please let me know if you need any additional information.\n\nThank you,\n[Your Name]",

        "retirement_announcement": "Dear [Name],\n\nI am writing to let you know that I will be retiring from my position at [Company] effective [Retirement Date]. I have enjoyed my time here and will cherish the memories.\n\nBest regards,\n[Your Name]",

        "congratulatory_note": "Hi [Name],\n\nI wanted to congratulate you on [Achievement]. Your hard work and dedication have truly paid off. Well done!\n\nBest wishes,\n[Your Name]"
    }
    
    # Default template if no match
    default_template = "Dear [Name],\n\nI hope this message finds you well. I wanted to discuss [Topic].\n\nBest regards,\n[Your Name]"
    
    for key in templates:
        if key in subject.lower():
            return templates[key]

    return default_template