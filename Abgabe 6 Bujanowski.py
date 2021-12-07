#!/usr/bin/env python
# coding: utf-8

# ### Abgabe 6 Evgeniya Bujanowski

# ### 1. Schauen Sie sich das Jupyter Notebook aus der Veranstaltung „Daten managen I“ an und vollziehen die Schritte aus dem Live-Coding bis zur Zusammenführung der Umwelt- und Wetterdaten noch einmal nach. 

# In[16]:


10 + 10


# In[17]:


20  / 10


# In[18]:


print("Hello World")


# In[19]:


pi = 3.14159


# In[20]:


sentence = "Data literacy is useful."


# In[21]:


sentence


# In[22]:


len(sentence)


# In[23]:


sentence.upper()


# In[24]:


sentence.count("a")


# In[25]:


sentence.replace("a", "A")


# In[26]:


list_of_numbers = [5, 9, 12, 34]


# In[27]:


list_of_numbers[0]


# ----------------------------------------------

# ### Reflektieren Sie Ihr Vorgehen und beantworten folgende Fragen: Was hat gut geklappt? Wenn Sie auf Fragen oder Probleme gestoßen sind, erläutern Sie diese kurz und beschreiben auch, welche Lösung Sie ggf. gefunden haben.

# Alles hat soweit normal geklappt, ich habe keine Fragen.

# ----------------------------------------------

# ### 2. Laden Sie mittels Python die folgende Datei mit vom Umweltbundesamt erhobenen Messdaten für die Station Köln Rodenkirchen (DENW059) herunter: 
# 
# ### https://raw.githubusercontent.com/konrad/DaLI_Basismodul_WiSe2021_2022/main/data/Rodenkirchen_processed.csv
# 
# ### Lesen Sie die heruntergeladenen Daten, mithilfe der Programmbibliothek pandas, in einen DataFrame‚ "rodenkirchen" ein.

# In[28]:


import pandas as pd


# In[29]:


import urllib.request


# In[30]:


rodenkirchen_url = "https://raw.githubusercontent.com/konrad/DaLI_Basismodul_WiSe2021_2022/main/data/Rodenkirchen_processed.csv"


# In[31]:


rodenkirchen_file = "rodenkirchen.csv"


# In[32]:


urllib.request.urlretrieve(rodenkirchen_url, rodenkirchen_file)


# In[33]:


rodenkirchen = pd.read_csv(rodenkirchen_file)


# In[34]:


rodenkirchen


# ------------------------

# ### Lassen Sie sich mit der method ‚describe‘ die Überblicksstatistiken zum DataFrame ‚rodenkirchen‘ anzeigen. 

# read the documentation https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html

# In[35]:


# Die Methode "describe" gibt ein Überblicksstatistiken für numerische Spalten zurück
rodenkirchen.describe()


# Aus Interesse schau ich mir die ersten 100 Ergebnisse an, vllt ist da etwas Spannendes zu sehen

# In[36]:


rodenkirchen.head(100)


# Ich sehe z.B. jetzt, dass es Felder ohne Inhalt ("-") gibt. 
# Ich kann noch einmal die Methode "describe" anwenden, allerdings dann die nicht existierenden Werte rausschmeißen.

# In[37]:


rodenkirchen_decribe = pd.read_csv(rodenkirchen_file, na_values=["-"])


# In[38]:


rodenkirchen_decribe.describe()


# ### Wählen Sie eine der Variablen, geben Sie diese an und beschreiben Sie welche Informationen für diese Variable (Spalte) von ‚describe‘ geliefert werden.

# Ich nehme die Spalte "Stickstoffdioxid (NO₂) Ein-Stunden-Mittelwert in µg/m³" (ab jetzt "Stickstoffdioxid" gennant). Dazu könnte ich Folgendes sagen:
# 
# count: 
# Im Vergleich zu der Anzahl von Reihen im df rodenkirchen ist die count-Angabe kleiner - 8737.000000 zu 8393.000000. Ich gehe davon aus, dass der Grund ist, dass es in der Spalte "Stickstoffdioxid" na_values gab.
# 
# mean vs. 50%: 
# Der Medianwert (mean) liegt bei 21.746408. Ich denke, 50% stehen für Durchschnittswert. Der Unterschied ist zwar da, aber er kommt mir nicht kritisch vor. Trotzdem ist es wichtig, den Medianwert zu ermitteln. Er ist, meine ich, verlässlicher als der Durchschnittswert, weil der Durchschnittswert durch ein paar Ausreißer geändert werden kann.
# 
# min: 
# min liegt hier bei 0.600000. Ich verstehe es so, dass man immer Stickstoffdioxid in der Luft hat, nur manchmal sind die Mengen sehr klein.

# ---------------------------------------------------------

# ### 3. Diskutieren Sie, wann und warum es sinnvoll sein kann, für die Datenanalyse eine Programmiersprache wie Python oder ähnliche Lösungen zu nutzen. 

# 1) Es ist einfacher, mit Python automatisierte Prozesse zu entwickeln. Damit kann man sich wiederholende Aufgaben erledigen.
# Mit Excel/ Excel VBA würde es unter Umständen auch gehen. Python ist eventuell mächtiges und schneller in dieser Hinsicht.

# 2) Python kann sehr große Datenmengen bearbeten, da kommt Excel je nach Aufgabe auf seine Grenzen.

# 3) Es gibt mehrere Bibliotheken für Visualisierungen in Python: plotly, seaborn, matpotlib etc. Damit lassen sich
# überzeugene Visualisierungen machen. Je nach Bibliothek kann man auch animierte Visualisierunngen erzeugen. Wenn fertig, 
# kann man eine Visualisierung als z.B. HTML oder als cvg (Scalable Vector Graphic) exportieren für weitere Schritte: 
# zum Embedden auf einer Webseite oder zur weiteren Bearbeitung im Adobe Illustrator.

# 4) In Python kann man auch sentimant analysis machen, NLP Projekte durchführen. Diese Sachen sind interessant für Journalisten, aber auch für Marketing-Exprterten. 

# 5) Excel kann unter Umständen eine Zahl z.B. als Datum interprtieren. Das kann zu Fehlern führen. 

# ------------------------------------------------------

# Random question: Wie kann die Luftqualität ausfallen?

# In[39]:


rodenkirchen["Luftqualitätsindex"].unique()


# Ok, die Luftqualitätsindex kann sehr gut, gut, mäßig und schlecht sein. 
