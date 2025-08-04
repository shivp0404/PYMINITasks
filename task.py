import datetime

class Task:

    def __init__(self,title,category="General",done=False):
        self.title = title
        self.category = category
        self.done = done
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mark_done(self):
        self.done = True

    def to_dict(self):
        return{
            "title":self.title,
            "category":self.category,
            "done":self.done,
            "created_at":self.created_at
        }
    
    @staticmethod
    def from_dict(data):
        task = Task(data['title'],data['category'],data['done'])
        task.created_at = data['created_at']
        return task;