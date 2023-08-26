###############_______________COLOR_CODES_______________###############___START
TRANSPARENT = 'systemTransparent'
WHITE = '#FFFFFF'
FADEDBLUE = '#3C88F4'
FADEDRED = '#F488C3'
BRIGHTBLUE = '#0000FF'
BRIGHTRED = '#FF0000'
DARKBLUE = '#0000A6'
DARKRED = '#A60000'
PRIMARYBLUE = '#2D69B9'
PRIMARYRED = DARKRED#'#B92D69'
SECONDARYBLUE = '#4496F8'
SECONDARYRED = FADEDRED
THEMEBLUE = '#C0EBFC'
DEFAULTBLUE = '#153765'
BACKGROUNDBLUE = '#2356C7'
BLACK = '#000000'
###############_______________COLOR_CODES_______________###############___END



###############_______________FONT_CODES_______________###############___START
startPageFont = ('Courier New', 35, 'bold')
startLanguagePageFont = ('Times New Roman', 20, 'bold', 'underline')
choicePageInfoFont = ('Times New Roman', 16)
choicePageBackFont = ('Courier New', 20, 'bold')
existingGridFont = ('Courier New', 35, 'bold')
enterNumbersFont = ('Courier New', 30, 'bold')
playInfoFont = ('Times New Roman', 15)
playNotesFont = ('Courier New', 10, 'bold')
missingInfoFont = ('Times New Roman', 13)
###############_______________FONT_CODES_______________###############___END



###############_______________LANGUAGE_TRANSLATIONS_______________###############___START
translatedText = {
    'titleMenu':{'English':'Sudoku - Menu', 'Français':'Sudoku - Menu', 'Deutsch':'Sudoku - Menü', 'Español':'Sudoku - Menú'},
    'titleDifficulty':{'English':'Sudoku - Difficulty', 'Français':'Sudoku - Difficulté', 'Deutsch':'Sudoku - Schwierigkeit', 'Español':'Sudoku - Dificultad'},
    'titleGenerate':{'English':'Sudoku - Generate', 'Français':'Sudoku - Générer', 'Deutsch':'Sudoku - Generieren', 'Español':'Sudoku - Generar'},
    'titleCreation':{'English':'Sudoku - Creation', 'Français':'Sudoku - Créer', 'Deutsch':'Sudoku - Erstellen', 'Español':'Sudoku - Crear'},
    'titleImport':{'English':'Sudoku - Save', 'Français':'Sudoku - Sauvegarder', 'Deutsch':'Sudoku - Speichern', 'Español':'Sudoku - Guardar'},
    'titlePlay':{'English':'Sudoku - Play', 'Français':'Sudoku - Jouer', 'Deutsch':'Sudoku - Spielen', 'Español':'Sudoku - Jugar'},
    'languageBT':{'English':'EN', 'Français':'FR', 'Deutsch':'DE', 'Español':'ES'}, 
    'startBT':{'English':'New Sudoku', 'Français':'Nouveau Sudoku', 'Deutsch':'Neues Sudoku', 'Español':'Nuevo sudoku'}, 
    'exitBT':{'English':'Quit Game', 'Français':'Quitter le Jeu', 'Deutsch':'Spiel Verlassen', 'Español':'Salir del juego'},
    'exploreBT':{'English':'Select Grid', 'Français':'Sélectionner Grille', 'Deutsch':'Wählen Raster', 'Español':'Seleccionar Caja'}, 
    'generateBT':{'English':'Generate Grid', 'Français':'Générer Grille', 'Deutsch':'Generieren Raster', 'Español':'Generar Caja'}, 
    'createBT':{'English':'Create Grid', 'Français':'Créer Grille', 'Deutsch':'Erstellen Raster', 'Español':'Crear Caja'}, 
    'importBT':{'English':'Import Grid', 'Français':'Importer Grille', 'Deutsch':'Importieren Raster', 'Español':'Importar Caja'}, 
    'importLB':{'English':'Select a File', 'Français':'Sélectionnez un fichier', 'Deutsch':'Wählen Sie eine Datei aus', 'Español':'Seleccione un archivo'},
    'importErrorLB':{'English':'⚠ The imported file contains an invalid sudoku.', 'Français':'⚠ Le fichier importé contient un sudoku invalide.', 'Deutsch':'⚠ Die importierte Datei enthält ein ungültiges Sudoku.', 'Español':'⚠ El archivo importado contiene un sudoku no válido.'},
    'backBT':{'English':'Back', 'Français':'Annuler', 'Deutsch':'Zurück', 'Español':'Anulador'},
    'difficultyVR':{'English':'Select the difficulty:', 'Français':'Choisir la difficulté:', 'Deutsch':'Schwierigkeitsgrad:', 'Español':'Anulador'}, 
    'confirmBT':{'English':'Confirm', 'Français':'Confirmer', 'Deutsch':'Bestätigen', 'Español':'Confirmar'}, 
    'sourceVR':{'English':'Select the Source:', 'Français':"Choisir l'origine:", 'Deutsch':'Wählen Quelle:', 'Español':'Seleccione Fuente'},
    'solveBT':{'English':'Solve', 'Français':'Résoudre', 'Deutsch':'Lösen', 'Español':'Anulador'},
    'verifyBT':{'English':'Verify', 'Français':'Fini', 'Deutsch':'Fertig', 'Español':'Resolver'},
    'resumeBT':{'English':'Resume', 'Français':'Reprendre', 'Deutsch':'Fortsetzen', 'Español':'Reanudar'},
    'abandonBT':{'English':'Quit', 'Français':'Fermer', 'Deutsch':'Stop', 'Español':'Detener'},
    'sourceET':{'English':'Origin of the Sudoku', 'Français':'Origine du Sudoku', 'Deutsch':'Ursprung Raster', 'Español':'Origen Caja'}, 
    'diffVR':{'English':'Difficulty:', 'Français':'Difficulté:', 'Deutsch':'Schwierigkeit:', 'Español':'Dificultad'},
    'srcET':{'English':'Sudoku Source:', 'Français':'Origine:', 'Deutsch':'Ursprung', 'Español':'Origen'},
    'finishedBT':{'English':'Finished', 'Français':'Terminé', 'Deutsch':'Fertig', 'Español':'Terminado'},
    'saveBT':{'English':'Save', 'Français':'Sauvegarder', 'Deutsch':'Speichern', 'Español':'Ahorrar'},
    'unexpectedError':{'English':'An unexpected error occurred, please try again.', 'Français':'Une erreur est survenue, veuillez ré-essayer.', 'Deutsch':'Ein unerwarteter Fehler aufgetreten. Bitte versuche es erneut.', 'Español':'Ocurrió un error inesperado, inténtalo de nuevo.'},
    'incompleteSudoku':{'English':"The Sudoku is missing numbers to be solvable !", 'Français':'Le Sudoku manque de nombres !', 'Deutsch':"Dem Sudoku fehlen Zahlen, um lösbar zu sein!", 'Español':'¡Al Sudoku le faltan números para ser solucionables!'},
    'missingInfo':{'English':'Some information is missing.', 'Français':'Il manque des informations.', 'Deutsch':'Einige Informationen fehlen.', 'Español':'Falta algo de información.'},
    'generatedSudoku':{'English':'Generated Sudoku', 'Français':'Sudoku Généré', 'Deutsch':'Generiert Sudoku', 'Español':'Sudoku Generado'}
    }

levelTranslated = {
    'Very Easy':{'English':'Very Easy', 'Français':'Très Facile', 'Deutsch':'Sehr leicht', 'Español':'Muy Fácil'}, 
    'Easy':{'English':'Easy', 'Français':'Facile', 'Deutsch':'Einfach', 'Español':'Fácil'}, 
    'Medium':{'English':'Medium', 'Français':'Moyen', 'Deutsch':'Normal', 'Español':'Normal'}, 
    'Hard':{'English':'Hard', 'Français':'Difficile', 'Deutsch':'Hart', 'Español':'Difícil'}, 
    'Very Hard':{'English':'Very Hard', 'Français':'Très Dur', 'Deutsch':'Sehr Schwer', 'Español':'Muy dificil'}, 
    'Impossible':{'English':'Impossible', 'Français':'Impossible', 'Deutsch':'Unmöglich', 'Español':'Imposible'}
    }

resultButton = {
    'solved':{'English':'The Sudoku is solved !', 'Français':'Le Sudoku a été résolu !', 'Deutsch':'Das Sudoku ist gelöst !', 'Español':'¡El Sudoku está resuelto!'}, 
    'incomplete':{'English':'The Sudoku is not fully completed !', 'Français':'Le Sudoku est incomplet !', 'Deutsch':'Das Sudoku ist noch nicht abgeschlossen !', 'Español':'¡El Sudoku no está completado!'}, 
    'false':{'English':'The Sudoku contains errors !', 'Français':'Le Sudoku contient des erreurs !', 'Deutsch':'Das Sudoku enthält Fehler !', 'Español':'¡El Sudoku contiene errores!'}, 
    '0hint':{'English':'All hints were used !', 'Français':'Toutes les aides ont été utilisées !', 'Deutsch':'Alle Hinweise wurden verwendet !', 'Español':'¡Todas las pistas fueron usadas!'}, 
    '1hint':{'English':'A hint was used, there is 1 left.', 'Français':'Une aide a été utilisé, il en reste 1.', 'Deutsch':'Es wurde ein Hinweis verwendet, es ist noch 1 übrig.', 'Español':'Se usó una pista, queda 1.'}, 
    '2hint':{'English':'A hint was used, there are 2 left.', 'Français':'Une aide a été utilisé, il en reste 2.', 'Deutsch':'Es wurde ein Hinweis verwendet, es sind noch 2 übrig.', 'Español':'Se usó una pista, quedan 2.'}
    }
###############_______________LANGUAGE_TRANSLATIONS_______________###############___END