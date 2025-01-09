# Vorlage für Watch

Batchdatei ruft Pythonfile auf \
Die Batchdatei muss (kann) ins Autostartverzeichnis ```C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup```

windows task scheduler

Here's how you can do it:

Open the Task Scheduler by pressing the Windows key + R and typing "taskschd.msc".

Click on "Create Task" in the right-hand pane.

Give the task a name and description.

In the "Triggers" tab, set up the schedule for when you want the task to run.

In the "Actions" tab, click "New" and then "Start a program".

In the "Program/script" field, type "python.exe".

In the "Add arguments (optional)" field, specify the path to your python file, for example: "script.py".

Check the "Hidden" box in the "Settings" tab to run the task in the background.

Click "OK" to save the task.

The Task Scheduler will now run your python file at the scheduled times in the background.

To run a python file when your computer restarts, you can use the Task Scheduler as described in my previous answer and set the task to run "At log on" in the "Triggers" tab.

This will ensure that the task is run every time you log into your Windows account, including after a restart.

## Oder

Aufgabenplanung öffnen

Aufgabe importieren (xml)
