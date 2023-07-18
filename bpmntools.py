import xmltodict
from bpmn_tools.flow          import Process, Start, End, Task, Flow
from bpmn_tools.collaboration import Collaboration, Participant
from bpmn_tools.notation      import Definitions
from bpmn_tools.diagrams      import Diagram, Plane, Shape, Edge
from bpmn_tools.layout        import simple

activities = [
  Start(id="start"),
  Task('Order Pizza', id="hello"),
  Task('Wait for response...', id="wait"),
  Task('Get Pizza', id = "get"),
  End(id="end")
]
process = Process(id="process").extend(activities).extend([
  Flow(source=activities[0], target=activities[1]),
  Flow(source=activities[1], target=activities[2]),
  Flow(source=activities[2], target=activities[3]),
  Flow(source=activities[3], target=activities[4]),
])
collaboration = Collaboration(id="collaboration").append(
  Participant("lane", process, id="participant")
)
model = Definitions(id="definitions").extend([
  process,
  collaboration,
])
model.append(
  Diagram(
    id="diagram",
    plane=Plane(id="plane", element=collaboration)
  )
)
Definitions({'id': 'definitions', 'xmlns:bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL', 'xmlns:bpmndi': 'http://www.omg.org/spec/BPMN/20100524/DI', 'xmlns:dc': 'http://www.omg.org/spec/DD/20100524/DC', 'xmlns:di': 'http://www.omg.org/spec/DD/20100524/DI'})
simple.layout(model)
xml = xmltodict.unparse(model.as_dict(with_tag=True), pretty=True)

with open("pizza.bpmn", "w") as fp:
  fp.write(xml)