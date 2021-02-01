from datetime import datetime

class location:
  def __init__(self, loc_id, hospital, building, floor, pod, room, created_at, updated_at):
    self.loc_id = loc_id
    self.hospital = hospital
    self.building = building
    self.floor = floor
    self.pod = pod
    self.room = room
    self.created_at = datetime.now()
    self.updated_at = updated_at

loc1 = location(1, 'LURIE', 'MAIN', 12, 'A', 120, datetime.now(), 'NULL')
loc2 = location(2, 'LURIE', 'C-D', 3, 'C', 10, datetime.now(), 'NULL')

print(loc1)
print(loc1.building)
print(loc2.created_at)

class resource:
  def __init__(self, user_id, hospital, deptartment, division, f_name, m_initial, l_name, email, created_at):
    self.user_id = user_id
    self.hospital = hospital
    self.deptartment = deptartment
    self.division = division
    self.f_name = f_name
    self.m_initial = m_initial
    self.l_name = l_name
    self.email = email
    self.created_at = datetime.now()

user1 = resource(1, 'LURIE', 'PEDIATRICS', 'CARDIOLOGY', 'CULLEN', 'B', 'DOLAN', 'cullen@gmail.com', datetime.now())
user2 = resource(2, 'LURIE', 'SURGERY', 'NEUROSURGERY', 'EMILY', 'K', 'RYAN', 'emily@gmail.com', datetime.now())
print(user1.division)