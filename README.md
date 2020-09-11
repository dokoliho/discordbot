# Discord Bot

## Vorbereitung

Im Developer-Portal von Discord ist eine neue App anzulegen. 

https://discord.com/developers/applications

Die Applikation erhält als nächstes einen Bot-User, der Servern beitreten kann. 
Dieser User besitzt ein Token, das später im Programmcode benötigt wird, 
um den Bot-Code mit diesem Bot-User zu verbinden bzw. damit sich der
Code als dieser Bot-User identifizieren kann. Wir speichern das Token in einer
separaten Datei .env, die nicht in die Versionsverwaltung mit eingecheckt wird (Security). 

## Einladen des Bots

Um den Bot auf einen Discord-Server zu bringen, muss die App eingeladen werden. 
Dazu benötigt man einen Einladungslink, den man im Abschnitt *OAuth2*
zusammenstellen kann. Scope sollte *bot* sein, Permissions wie benötigt.
Das Ergebnis ist ein Einladungslink

https://discord.com/api/oauth2/authorize?client_id=<ID der App>&permissions=24641088&scope=bot

Öffnet man die URL im Browser, werden alle Server angeboten, die der aktuelle User verwalten darf. 

Sobald man den Bot autorisiert, wird er als offline angezeigt.

## Starten des Bots

Sobald man das Python-Skript startet, geht der Bot online. Die Beispielimplementierung 
überwacht alle Kanäle auf die Nachricht "?test" und antwortet mit einem "Ok". Natürlich 
muss man für die Kanäle berechtigt sein.

Bei einer konkreten Anwendung wird man unterscheiden müssen
- auf welchem Server wurde die Nachricht geschrieben
- auf welchem Kanal wurde die Nachricht geschrieben
- wer hat die Nachricht geschrieben etc.

Dazu bietet der Python-Wrapper für die Discord-Api einige Objekte mit 
entsprechenden Funktionen.

https://discordpy.readthedocs.io/en/latest/index.html




