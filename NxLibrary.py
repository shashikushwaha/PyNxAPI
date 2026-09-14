import sys
sys.path.append(r"C:\Program Files\Siemens\NX 12.0\NXBIN\python")
import math
import NXOpen
class NXSession:
    def __init__(self):
        self.session = NXOpen.Session.GetSession()

    def open_part(self, file_path):
        try:
            work_part = self.session.Parts.OpenActiveDisplay(file_path, NXOpen.DisplayPartOption.AllowAdditional)
            return work_part
        except NXOpen.NXException as e:
            print(f"Failed to open part file: {e.Message}")
            return None

    def get_bodies(self):
            bodies = NXOpen.Session.GetSession().Parts.Work.Bodies
            all_bodies = []
            for one_body in bodies:
                all_bodies.append(one_body)
            #print(all_bodies)
            return all_bodies

    def get_parts(self):
        return self.session.Parts

