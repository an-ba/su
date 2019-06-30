import yaml #PyYAML
import random



aktion1 = ["debugge", "teste"]
aktion2 = ["die Nacharbeiten", "den Code-Review", "die Nacharbeiten"]
objekt = ["zur Zwischenschicht", "zum Formular-Layer", "für das Abbrechermailing"]
reason = ["es in der Queue hochgerutscht ist", "es in der Queue runtergerutscht ist", "es jetzt hochpriorisiert wurde", "es jetzt runterpriorisiert wurde"]
nachsatz = ["An der Stelle.", "Habe ich etwa Peakwork gesagt??", "Und dann schaue ich noch was in der Queue liegt"]

output = f"Ich {random.choice(aktion1)} {random.choice(aktion2)}  {random.choice(objekt)},weil {random.choice(reason)}. {random.choice(nachsatz)}"


print(output)