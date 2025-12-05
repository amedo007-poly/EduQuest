"""Seed data - Sample quizzes and questions across multiple subjects"""

SAMPLE_QUIZZES = [
    # ============== MATHEMATICS ==============
    {
        "title": "🔢 Mathématiques - Les bases",
        "subject": "math",
        "level_required": 1,
        "questions": [
            {
                "question_text": "Combien font 7 + 5 ?",
                "option_a": "10",
                "option_b": "11",
                "option_c": "12",
                "option_d": "13",
                "correct_option": "C"
            },
            {
                "question_text": "Quel est le résultat de 15 - 8 ?",
                "option_a": "5",
                "option_b": "6",
                "option_c": "7",
                "option_d": "8",
                "correct_option": "C"
            },
            {
                "question_text": "Combien font 4 × 6 ?",
                "option_a": "20",
                "option_b": "24",
                "option_c": "26",
                "option_d": "28",
                "correct_option": "B"
            },
            {
                "question_text": "Quel est le carré de 5 ?",
                "option_a": "10",
                "option_b": "15",
                "option_c": "20",
                "option_d": "25",
                "correct_option": "D"
            },
            {
                "question_text": "Combien font 36 ÷ 6 ?",
                "option_a": "4",
                "option_b": "5",
                "option_c": "6",
                "option_d": "7",
                "correct_option": "C"
            }
        ]
    },
    {
        "title": "🔢 Mathématiques - Intermédiaire",
        "subject": "math",
        "level_required": 2,
        "questions": [
            {
                "question_text": "Résoudre: 2x + 4 = 10. Que vaut x ?",
                "option_a": "2",
                "option_b": "3",
                "option_c": "4",
                "option_d": "5",
                "correct_option": "B"
            },
            {
                "question_text": "Quel est le PGCD de 12 et 18 ?",
                "option_a": "2",
                "option_b": "3",
                "option_c": "6",
                "option_d": "9",
                "correct_option": "C"
            },
            {
                "question_text": "Combien font 15% de 200 ?",
                "option_a": "20",
                "option_b": "25",
                "option_c": "30",
                "option_d": "35",
                "correct_option": "C"
            },
            {
                "question_text": "Quelle est la racine carrée de 144 ?",
                "option_a": "10",
                "option_b": "11",
                "option_c": "12",
                "option_d": "14",
                "correct_option": "C"
            },
            {
                "question_text": "Si un triangle a des côtés 3, 4, 5, est-il rectangle ?",
                "option_a": "Oui",
                "option_b": "Non",
                "option_c": "Impossible à dire",
                "option_d": "Seulement si isocèle",
                "correct_option": "A"
            }
        ]
    },
    {
        "title": "🔢 Mathématiques - Avancé",
        "subject": "math",
        "level_required": 3,
        "questions": [
            {
                "question_text": "Quelle est la dérivée de x² ?",
                "option_a": "x",
                "option_b": "2x",
                "option_c": "x²",
                "option_d": "2",
                "correct_option": "B"
            },
            {
                "question_text": "Que vaut sin(90°) ?",
                "option_a": "0",
                "option_b": "0.5",
                "option_c": "1",
                "option_d": "-1",
                "correct_option": "C"
            },
            {
                "question_text": "Quelle est l'intégrale de 2x ?",
                "option_a": "x",
                "option_b": "x²",
                "option_c": "x² + C",
                "option_d": "2x²",
                "correct_option": "C"
            },
            {
                "question_text": "Combien vaut log₁₀(1000) ?",
                "option_a": "2",
                "option_b": "3",
                "option_c": "10",
                "option_d": "100",
                "correct_option": "B"
            },
            {
                "question_text": "Dans une suite géométrique de raison 2 et premier terme 3, quel est le 4ème terme ?",
                "option_a": "12",
                "option_b": "18",
                "option_c": "24",
                "option_d": "48",
                "correct_option": "C"
            }
        ]
    },
    
    # ============== FRENCH ==============
    {
        "title": "📖 Français - Grammaire",
        "subject": "french",
        "level_required": 1,
        "questions": [
            {
                "question_text": "Quel est le pluriel de 'cheval' ?",
                "option_a": "Chevals",
                "option_b": "Chevaux",
                "option_c": "Chevales",
                "option_d": "Chevauxs",
                "correct_option": "B"
            },
            {
                "question_text": "Dans 'Le chat mange', quel est le sujet ?",
                "option_a": "mange",
                "option_b": "Le",
                "option_c": "Le chat",
                "option_d": "chat mange",
                "correct_option": "C"
            },
            {
                "question_text": "Quel temps est 'Je mangeais' ?",
                "option_a": "Présent",
                "option_b": "Passé composé",
                "option_c": "Imparfait",
                "option_d": "Futur",
                "correct_option": "C"
            },
            {
                "question_text": "Comment s'appelle le signe '?' ?",
                "option_a": "Point d'exclamation",
                "option_b": "Point d'interrogation",
                "option_c": "Point-virgule",
                "option_d": "Deux-points",
                "correct_option": "B"
            },
            {
                "question_text": "'Rapidement' est quel type de mot ?",
                "option_a": "Adjectif",
                "option_b": "Verbe",
                "option_c": "Adverbe",
                "option_d": "Nom",
                "correct_option": "C"
            }
        ]
    },
    {
        "title": "📖 Français - Conjugaison",
        "subject": "french",
        "level_required": 2,
        "questions": [
            {
                "question_text": "Conjuguez 'finir' au passé composé (je) :",
                "option_a": "J'ai fini",
                "option_b": "Je finissais",
                "option_c": "Je finis",
                "option_d": "J'avais fini",
                "correct_option": "A"
            },
            {
                "question_text": "Quel est le participe passé de 'prendre' ?",
                "option_a": "Prenu",
                "option_b": "Pris",
                "option_c": "Prendu",
                "option_d": "Prendre",
                "correct_option": "B"
            },
            {
                "question_text": "'Nous courrons' est à quel temps ?",
                "option_a": "Présent",
                "option_b": "Imparfait",
                "option_c": "Futur simple",
                "option_d": "Conditionnel",
                "correct_option": "C"
            },
            {
                "question_text": "Subjonctif présent de 'être' (que je) :",
                "option_a": "que je suis",
                "option_b": "que je sois",
                "option_c": "que je serai",
                "option_d": "que j'étais",
                "correct_option": "B"
            },
            {
                "question_text": "'Il fallait' est à quel temps ?",
                "option_a": "Présent",
                "option_b": "Passé simple",
                "option_c": "Imparfait",
                "option_d": "Plus-que-parfait",
                "correct_option": "C"
            }
        ]
    },
    {
        "title": "📖 Français - Littérature",
        "subject": "french",
        "level_required": 3,
        "questions": [
            {
                "question_text": "Qui a écrit 'Les Misérables' ?",
                "option_a": "Émile Zola",
                "option_b": "Victor Hugo",
                "option_c": "Gustave Flaubert",
                "option_d": "Honoré de Balzac",
                "correct_option": "B"
            },
            {
                "question_text": "Quel mouvement littéraire est associé à Baudelaire ?",
                "option_a": "Romantisme",
                "option_b": "Réalisme",
                "option_c": "Symbolisme",
                "option_d": "Naturalisme",
                "correct_option": "C"
            },
            {
                "question_text": "Qu'est-ce qu'un alexandrin ?",
                "option_a": "Un vers de 10 syllabes",
                "option_b": "Un vers de 12 syllabes",
                "option_c": "Un vers de 8 syllabes",
                "option_d": "Un vers libre",
                "correct_option": "B"
            },
            {
                "question_text": "Qui est l'auteur de 'Le Petit Prince' ?",
                "option_a": "Jules Verne",
                "option_b": "Marcel Proust",
                "option_c": "Antoine de Saint-Exupéry",
                "option_d": "Albert Camus",
                "correct_option": "C"
            },
            {
                "question_text": "Quel siècle est appelé 'Le Siècle des Lumières' ?",
                "option_a": "16ème siècle",
                "option_b": "17ème siècle",
                "option_c": "18ème siècle",
                "option_d": "19ème siècle",
                "correct_option": "C"
            }
        ]
    },
    
    # ============== SCIENCE ==============
    {
        "title": "🔬 Sciences - Culture Générale",
        "subject": "science",
        "level_required": 1,
        "questions": [
            {
                "question_text": "Quelle planète est la plus proche du Soleil ?",
                "option_a": "Vénus",
                "option_b": "Mercure",
                "option_c": "Mars",
                "option_d": "Terre",
                "correct_option": "B"
            },
            {
                "question_text": "Quel gaz respirons-nous principalement ?",
                "option_a": "Oxygène",
                "option_b": "Azote",
                "option_c": "CO2",
                "option_d": "Hydrogène",
                "correct_option": "B"
            },
            {
                "question_text": "Combien d'os a le corps humain adulte ?",
                "option_a": "186",
                "option_b": "196",
                "option_c": "206",
                "option_d": "216",
                "correct_option": "C"
            },
            {
                "question_text": "Quel est le symbole chimique de l'eau ?",
                "option_a": "O2",
                "option_b": "H2O",
                "option_c": "CO2",
                "option_d": "HO",
                "correct_option": "B"
            },
            {
                "question_text": "Quelle est la vitesse de la lumière ?",
                "option_a": "300 km/s",
                "option_b": "3 000 km/s",
                "option_c": "30 000 km/s",
                "option_d": "300 000 km/s",
                "correct_option": "D"
            }
        ]
    },
    {
        "title": "🔬 Physique - Mécanique",
        "subject": "science",
        "level_required": 2,
        "questions": [
            {
                "question_text": "Quelle est l'unité de force dans le SI ?",
                "option_a": "Joule",
                "option_b": "Watt",
                "option_c": "Newton",
                "option_d": "Pascal",
                "correct_option": "C"
            },
            {
                "question_text": "F = m × a est la formule de quelle loi ?",
                "option_a": "1ère loi de Newton",
                "option_b": "2ème loi de Newton",
                "option_c": "3ème loi de Newton",
                "option_d": "Loi de Hooke",
                "correct_option": "B"
            },
            {
                "question_text": "Quelle est l'accélération de la pesanteur sur Terre ?",
                "option_a": "8.9 m/s²",
                "option_b": "9.8 m/s²",
                "option_c": "10.8 m/s²",
                "option_d": "11.8 m/s²",
                "correct_option": "B"
            },
            {
                "question_text": "L'énergie cinétique se calcule avec :",
                "option_a": "E = mgh",
                "option_b": "E = ½mv²",
                "option_c": "E = mc²",
                "option_d": "E = Fd",
                "correct_option": "B"
            },
            {
                "question_text": "Qu'est-ce qu'un mouvement rectiligne uniforme ?",
                "option_a": "Vitesse variable, trajectoire droite",
                "option_b": "Vitesse constante, trajectoire courbe",
                "option_c": "Vitesse constante, trajectoire droite",
                "option_d": "Vitesse variable, trajectoire courbe",
                "correct_option": "C"
            }
        ]
    },
    {
        "title": "🧪 Chimie - Les bases",
        "subject": "science",
        "level_required": 2,
        "questions": [
            {
                "question_text": "Combien d'électrons a un atome de carbone ?",
                "option_a": "4",
                "option_b": "6",
                "option_c": "8",
                "option_d": "12",
                "correct_option": "B"
            },
            {
                "question_text": "Quel est le pH d'une solution neutre ?",
                "option_a": "0",
                "option_b": "5",
                "option_c": "7",
                "option_d": "14",
                "correct_option": "C"
            },
            {
                "question_text": "NaCl est le symbole de :",
                "option_a": "Sel de table",
                "option_b": "Sucre",
                "option_c": "Bicarbonate",
                "option_d": "Vinaigre",
                "correct_option": "A"
            },
            {
                "question_text": "Quel élément a pour symbole 'Fe' ?",
                "option_a": "Fluor",
                "option_b": "Fer",
                "option_c": "Francium",
                "option_d": "Fermium",
                "correct_option": "B"
            },
            {
                "question_text": "Une réaction exothermique :",
                "option_a": "Absorbe de la chaleur",
                "option_b": "Libère de la chaleur",
                "option_c": "N'échange pas de chaleur",
                "option_d": "Produit de la lumière",
                "correct_option": "B"
            }
        ]
    },
    {
        "title": "🧬 Biologie - Corps Humain",
        "subject": "science",
        "level_required": 2,
        "questions": [
            {
                "question_text": "Quel organe produit l'insuline ?",
                "option_a": "Foie",
                "option_b": "Rein",
                "option_c": "Pancréas",
                "option_d": "Estomac",
                "correct_option": "C"
            },
            {
                "question_text": "Combien de chromosomes a une cellule humaine normale ?",
                "option_a": "23",
                "option_b": "44",
                "option_c": "46",
                "option_d": "48",
                "correct_option": "C"
            },
            {
                "question_text": "Quel est le plus grand organe du corps humain ?",
                "option_a": "Le foie",
                "option_b": "Le cerveau",
                "option_c": "La peau",
                "option_d": "L'intestin",
                "correct_option": "C"
            },
            {
                "question_text": "Les globules rouges transportent :",
                "option_a": "Les nutriments",
                "option_b": "L'oxygène",
                "option_c": "Les anticorps",
                "option_d": "Les hormones",
                "correct_option": "B"
            },
            {
                "question_text": "L'ADN se trouve principalement dans :",
                "option_a": "Le cytoplasme",
                "option_b": "La membrane",
                "option_c": "Le noyau",
                "option_d": "Les ribosomes",
                "correct_option": "C"
            }
        ]
    },
    
    # ============== HISTORY ==============
    {
        "title": "📜 Histoire - Antiquité",
        "subject": "history",
        "level_required": 1,
        "questions": [
            {
                "question_text": "Quelle civilisation a construit les pyramides de Gizeh ?",
                "option_a": "Les Romains",
                "option_b": "Les Grecs",
                "option_c": "Les Égyptiens",
                "option_d": "Les Perses",
                "correct_option": "C"
            },
            {
                "question_text": "Qui était le premier empereur romain ?",
                "option_a": "Jules César",
                "option_b": "Auguste",
                "option_c": "Néron",
                "option_d": "Marc Antoine",
                "correct_option": "B"
            },
            {
                "question_text": "La démocratie est née dans quelle cité antique ?",
                "option_a": "Rome",
                "option_b": "Sparte",
                "option_c": "Athènes",
                "option_d": "Carthage",
                "correct_option": "C"
            },
            {
                "question_text": "Alexandre le Grand était roi de :",
                "option_a": "Perse",
                "option_b": "Macédoine",
                "option_c": "Égypte",
                "option_d": "Babylone",
                "correct_option": "B"
            },
            {
                "question_text": "Quel fleuve traverse l'Égypte ancienne ?",
                "option_a": "Le Tigre",
                "option_b": "L'Euphrate",
                "option_c": "Le Nil",
                "option_d": "Le Jourdain",
                "correct_option": "C"
            }
        ]
    },
    {
        "title": "📜 Histoire - Moyen Âge",
        "subject": "history",
        "level_required": 2,
        "questions": [
            {
                "question_text": "En quelle année Charlemagne a-t-il été couronné empereur ?",
                "option_a": "700",
                "option_b": "800",
                "option_c": "900",
                "option_d": "1000",
                "correct_option": "B"
            },
            {
                "question_text": "Combien de croisades majeures y a-t-il eu ?",
                "option_a": "5",
                "option_b": "7",
                "option_c": "8",
                "option_d": "10",
                "correct_option": "C"
            },
            {
                "question_text": "La Guerre de Cent Ans opposait :",
                "option_a": "France et Espagne",
                "option_b": "France et Angleterre",
                "option_c": "Angleterre et Allemagne",
                "option_d": "France et Italie",
                "correct_option": "B"
            },
            {
                "question_text": "Qui était Jeanne d'Arc ?",
                "option_a": "Une reine de France",
                "option_b": "Une héroïne militaire",
                "option_c": "Une philosophe",
                "option_d": "Une artiste",
                "correct_option": "B"
            },
            {
                "question_text": "La peste noire a frappé l'Europe au :",
                "option_a": "12ème siècle",
                "option_b": "13ème siècle",
                "option_c": "14ème siècle",
                "option_d": "15ème siècle",
                "correct_option": "C"
            }
        ]
    },
    {
        "title": "📜 Histoire - XXème Siècle",
        "subject": "history",
        "level_required": 3,
        "questions": [
            {
                "question_text": "En quelle année a commencé la Première Guerre mondiale ?",
                "option_a": "1912",
                "option_b": "1914",
                "option_c": "1916",
                "option_d": "1918",
                "correct_option": "B"
            },
            {
                "question_text": "Quel événement a déclenché la Seconde Guerre mondiale ?",
                "option_a": "Invasion de la Pologne",
                "option_b": "Pearl Harbor",
                "option_c": "Traité de Versailles",
                "option_d": "Crise de 1929",
                "correct_option": "A"
            },
            {
                "question_text": "Quand le mur de Berlin est-il tombé ?",
                "option_a": "1985",
                "option_b": "1987",
                "option_c": "1989",
                "option_d": "1991",
                "correct_option": "C"
            },
            {
                "question_text": "Qui a prononcé le discours 'I have a dream' ?",
                "option_a": "John F. Kennedy",
                "option_b": "Malcolm X",
                "option_c": "Martin Luther King Jr.",
                "option_d": "Barack Obama",
                "correct_option": "C"
            },
            {
                "question_text": "L'ONU a été créée en :",
                "option_a": "1918",
                "option_b": "1939",
                "option_c": "1945",
                "option_d": "1950",
                "correct_option": "C"
            }
        ]
    },
    
    # ============== GEOGRAPHY ==============
    {
        "title": "🌍 Géographie - Capitales du Monde",
        "subject": "geography",
        "level_required": 1,
        "questions": [
            {
                "question_text": "Quelle est la capitale de l'Australie ?",
                "option_a": "Sydney",
                "option_b": "Melbourne",
                "option_c": "Canberra",
                "option_d": "Brisbane",
                "correct_option": "C"
            },
            {
                "question_text": "Quelle est la capitale du Canada ?",
                "option_a": "Toronto",
                "option_b": "Montréal",
                "option_c": "Vancouver",
                "option_d": "Ottawa",
                "correct_option": "D"
            },
            {
                "question_text": "Quelle est la capitale du Brésil ?",
                "option_a": "Rio de Janeiro",
                "option_b": "São Paulo",
                "option_c": "Brasília",
                "option_d": "Salvador",
                "correct_option": "C"
            },
            {
                "question_text": "Quelle est la capitale de l'Inde ?",
                "option_a": "Mumbai",
                "option_b": "New Delhi",
                "option_c": "Bangalore",
                "option_d": "Calcutta",
                "correct_option": "B"
            },
            {
                "question_text": "Quelle est la capitale de l'Égypte ?",
                "option_a": "Alexandrie",
                "option_b": "Louxor",
                "option_c": "Le Caire",
                "option_d": "Assouan",
                "correct_option": "C"
            }
        ]
    },
    {
        "title": "🌍 Géographie - Relief et Océans",
        "subject": "geography",
        "level_required": 2,
        "questions": [
            {
                "question_text": "Quel est le plus haut sommet du monde ?",
                "option_a": "K2",
                "option_b": "Mont Blanc",
                "option_c": "Everest",
                "option_d": "Kilimandjaro",
                "correct_option": "C"
            },
            {
                "question_text": "Quel est le plus grand océan ?",
                "option_a": "Atlantique",
                "option_b": "Pacifique",
                "option_c": "Indien",
                "option_d": "Arctique",
                "correct_option": "B"
            },
            {
                "question_text": "Le Sahara est situé sur quel continent ?",
                "option_a": "Asie",
                "option_b": "Amérique",
                "option_c": "Afrique",
                "option_d": "Océanie",
                "correct_option": "C"
            },
            {
                "question_text": "Quel fleuve traverse Paris ?",
                "option_a": "Le Rhône",
                "option_b": "La Loire",
                "option_c": "La Seine",
                "option_d": "La Garonne",
                "correct_option": "C"
            },
            {
                "question_text": "L'Amazone se trouve sur quel continent ?",
                "option_a": "Afrique",
                "option_b": "Asie",
                "option_c": "Amérique du Sud",
                "option_d": "Amérique du Nord",
                "correct_option": "C"
            }
        ]
    },
    
    # ============== PROGRAMMING ==============
    {
        "title": "💻 Programmation - Les bases",
        "subject": "programming",
        "level_required": 1,
        "questions": [
            {
                "question_text": "Que signifie HTML ?",
                "option_a": "Hyper Text Markup Language",
                "option_b": "High Tech Modern Language",
                "option_c": "Home Tool Markup Language",
                "option_d": "Hyperlinks Text Mark Language",
                "correct_option": "A"
            },
            {
                "question_text": "Quel symbole commence un commentaire en Python ?",
                "option_a": "//",
                "option_b": "/*",
                "option_c": "#",
                "option_d": "--",
                "correct_option": "C"
            },
            {
                "question_text": "Qu'est-ce qu'une variable ?",
                "option_a": "Un type de boucle",
                "option_b": "Un espace de stockage nommé",
                "option_c": "Une fonction",
                "option_d": "Un opérateur",
                "correct_option": "B"
            },
            {
                "question_text": "Quel langage est principalement utilisé pour le style des pages web ?",
                "option_a": "JavaScript",
                "option_b": "Python",
                "option_c": "CSS",
                "option_d": "PHP",
                "correct_option": "C"
            },
            {
                "question_text": "Que fait une boucle 'for' ?",
                "option_a": "Teste une condition",
                "option_b": "Répète du code un nombre défini de fois",
                "option_c": "Définit une fonction",
                "option_d": "Importe un module",
                "correct_option": "B"
            }
        ]
    },
    {
        "title": "💻 Programmation - Python",
        "subject": "programming",
        "level_required": 2,
        "questions": [
            {
                "question_text": "Comment créer une liste vide en Python ?",
                "option_a": "list = {}",
                "option_b": "list = []",
                "option_c": "list = ()",
                "option_d": "list = new List()",
                "correct_option": "B"
            },
            {
                "question_text": "Quelle fonction affiche du texte en Python ?",
                "option_a": "echo()",
                "option_b": "console.log()",
                "option_c": "print()",
                "option_d": "write()",
                "correct_option": "C"
            },
            {
                "question_text": "Comment définir une fonction en Python ?",
                "option_a": "function maFonction():",
                "option_b": "def maFonction():",
                "option_c": "func maFonction():",
                "option_d": "define maFonction():",
                "correct_option": "B"
            },
            {
                "question_text": "Quel opérateur teste l'égalité en Python ?",
                "option_a": "=",
                "option_b": "===",
                "option_c": "==",
                "option_d": ":=",
                "correct_option": "C"
            },
            {
                "question_text": "Comment accéder au dernier élément d'une liste ?",
                "option_a": "liste[last]",
                "option_b": "liste[-1]",
                "option_c": "liste[len-1]",
                "option_d": "liste.last()",
                "correct_option": "B"
            }
        ]
    },
    {
        "title": "💻 Programmation - JavaScript",
        "subject": "programming",
        "level_required": 2,
        "questions": [
            {
                "question_text": "Comment déclarer une constante en JavaScript moderne ?",
                "option_a": "var x = 5",
                "option_b": "let x = 5",
                "option_c": "const x = 5",
                "option_d": "constant x = 5",
                "correct_option": "C"
            },
            {
                "question_text": "Quelle méthode ajoute un élément à la fin d'un tableau ?",
                "option_a": "add()",
                "option_b": "append()",
                "option_c": "push()",
                "option_d": "insert()",
                "correct_option": "C"
            },
            {
                "question_text": "Comment écrire une fonction fléchée ?",
                "option_a": "function => {}",
                "option_b": "() => {}",
                "option_c": "-> () {}",
                "option_d": "=> function() {}",
                "correct_option": "B"
            },
            {
                "question_text": "Que retourne typeof null ?",
                "option_a": "null",
                "option_b": "undefined",
                "option_c": "object",
                "option_d": "boolean",
                "correct_option": "C"
            },
            {
                "question_text": "Comment sélectionner un élément par ID ?",
                "option_a": "document.query('#id')",
                "option_b": "document.getElementById('id')",
                "option_c": "document.select('#id')",
                "option_d": "document.find('id')",
                "correct_option": "B"
            }
        ]
    },
    {
        "title": "💻 Programmation - Algorithmes",
        "subject": "programming",
        "level_required": 3,
        "questions": [
            {
                "question_text": "Quelle est la complexité de la recherche binaire ?",
                "option_a": "O(1)",
                "option_b": "O(n)",
                "option_c": "O(log n)",
                "option_d": "O(n²)",
                "correct_option": "C"
            },
            {
                "question_text": "Quel algorithme de tri a la meilleure complexité moyenne ?",
                "option_a": "Bubble Sort",
                "option_b": "Quick Sort",
                "option_c": "Selection Sort",
                "option_d": "Insertion Sort",
                "correct_option": "B"
            },
            {
                "question_text": "Qu'est-ce qu'une fonction récursive ?",
                "option_a": "Une fonction qui s'appelle elle-même",
                "option_b": "Une fonction asynchrone",
                "option_c": "Une fonction anonyme",
                "option_d": "Une fonction pure",
                "correct_option": "A"
            },
            {
                "question_text": "Quelle structure utilise FIFO ?",
                "option_a": "Stack (Pile)",
                "option_b": "Queue (File)",
                "option_c": "Tree (Arbre)",
                "option_d": "Graph (Graphe)",
                "correct_option": "B"
            },
            {
                "question_text": "Le Big O de l'accès à un élément dans un tableau est :",
                "option_a": "O(1)",
                "option_b": "O(n)",
                "option_c": "O(log n)",
                "option_d": "O(n log n)",
                "correct_option": "A"
            }
        ]
    },
    
    # ============== ENGLISH ==============
    {
        "title": "🇬🇧 English - Vocabulary",
        "subject": "english",
        "level_required": 1,
        "questions": [
            {
                "question_text": "What is the opposite of 'happy'?",
                "option_a": "Angry",
                "option_b": "Sad",
                "option_c": "Excited",
                "option_d": "Tired",
                "correct_option": "B"
            },
            {
                "question_text": "'Beautiful' is a/an:",
                "option_a": "Noun",
                "option_b": "Verb",
                "option_c": "Adjective",
                "option_d": "Adverb",
                "correct_option": "C"
            },
            {
                "question_text": "What does 'enormous' mean?",
                "option_a": "Very small",
                "option_b": "Very big",
                "option_c": "Very fast",
                "option_d": "Very old",
                "correct_option": "B"
            },
            {
                "question_text": "The plural of 'child' is:",
                "option_a": "Childs",
                "option_b": "Childen",
                "option_c": "Children",
                "option_d": "Childes",
                "correct_option": "C"
            },
            {
                "question_text": "'Quickly' is a/an:",
                "option_a": "Noun",
                "option_b": "Verb",
                "option_c": "Adjective",
                "option_d": "Adverb",
                "correct_option": "D"
            }
        ]
    },
    {
        "title": "🇬🇧 English - Grammar",
        "subject": "english",
        "level_required": 2,
        "questions": [
            {
                "question_text": "Choose the correct form: 'She ___ to school every day.'",
                "option_a": "go",
                "option_b": "goes",
                "option_c": "going",
                "option_d": "gone",
                "correct_option": "B"
            },
            {
                "question_text": "What is the past tense of 'eat'?",
                "option_a": "Eated",
                "option_b": "Eaten",
                "option_c": "Ate",
                "option_d": "Eating",
                "correct_option": "C"
            },
            {
                "question_text": "'I have been waiting for 2 hours' is in which tense?",
                "option_a": "Present Simple",
                "option_b": "Present Perfect",
                "option_c": "Present Perfect Continuous",
                "option_d": "Past Perfect",
                "correct_option": "C"
            },
            {
                "question_text": "Choose the correct sentence:",
                "option_a": "He don't like coffee",
                "option_b": "He doesn't likes coffee",
                "option_c": "He doesn't like coffee",
                "option_d": "He not like coffee",
                "correct_option": "C"
            },
            {
                "question_text": "'If I were you, I would go' is a:",
                "option_a": "First conditional",
                "option_b": "Second conditional",
                "option_c": "Third conditional",
                "option_d": "Zero conditional",
                "correct_option": "B"
            }
        ]
    },
    
    # ============== MUSIC ==============
    {
        "title": "🎵 Musique - Culture Générale",
        "subject": "music",
        "level_required": 1,
        "questions": [
            {
                "question_text": "Combien de notes y a-t-il dans une gamme majeure ?",
                "option_a": "5",
                "option_b": "6",
                "option_c": "7",
                "option_d": "8",
                "correct_option": "C"
            },
            {
                "question_text": "Qui a composé 'La Lettre à Élise' ?",
                "option_a": "Mozart",
                "option_b": "Bach",
                "option_c": "Beethoven",
                "option_d": "Chopin",
                "correct_option": "C"
            },
            {
                "question_text": "Quel instrument a 88 touches ?",
                "option_a": "Guitare",
                "option_b": "Piano",
                "option_c": "Violon",
                "option_d": "Accordéon",
                "correct_option": "B"
            },
            {
                "question_text": "Combien de cordes a une guitare standard ?",
                "option_a": "4",
                "option_b": "5",
                "option_c": "6",
                "option_d": "7",
                "correct_option": "C"
            },
            {
                "question_text": "Quel est le tempo 'Allegro' ?",
                "option_a": "Très lent",
                "option_b": "Lent",
                "option_c": "Modéré",
                "option_d": "Rapide",
                "correct_option": "D"
            }
        ]
    },
    
    # ============== SPORTS ==============
    {
        "title": "⚽ Sports - Culture Générale",
        "subject": "sports",
        "level_required": 1,
        "questions": [
            {
                "question_text": "Combien de joueurs y a-t-il dans une équipe de football ?",
                "option_a": "9",
                "option_b": "10",
                "option_c": "11",
                "option_d": "12",
                "correct_option": "C"
            },
            {
                "question_text": "Tous les combien d'années ont lieu les Jeux Olympiques ?",
                "option_a": "2 ans",
                "option_b": "3 ans",
                "option_c": "4 ans",
                "option_d": "5 ans",
                "correct_option": "C"
            },
            {
                "question_text": "Dans quel sport utilise-t-on un volant ?",
                "option_a": "Tennis",
                "option_b": "Badminton",
                "option_c": "Ping-pong",
                "option_d": "Squash",
                "correct_option": "B"
            },
            {
                "question_text": "Un marathon fait combien de kilomètres ?",
                "option_a": "21 km",
                "option_b": "35 km",
                "option_c": "42 km",
                "option_d": "50 km",
                "correct_option": "C"
            },
            {
                "question_text": "Combien de sets faut-il gagner en tennis masculin Grand Chelem ?",
                "option_a": "2",
                "option_b": "3",
                "option_c": "4",
                "option_d": "5",
                "correct_option": "B"
            }
        ]
    },
    
    # ============== ART ==============
    {
        "title": "🎨 Art - Histoire de l'Art",
        "subject": "art",
        "level_required": 1,
        "questions": [
            {
                "question_text": "Qui a peint 'La Joconde' ?",
                "option_a": "Michel-Ange",
                "option_b": "Raphaël",
                "option_c": "Léonard de Vinci",
                "option_d": "Botticelli",
                "correct_option": "C"
            },
            {
                "question_text": "Dans quel musée se trouve 'La Joconde' ?",
                "option_a": "Le British Museum",
                "option_b": "Le Louvre",
                "option_c": "Le Prado",
                "option_d": "Les Offices",
                "correct_option": "B"
            },
            {
                "question_text": "Qui a peint 'Les Tournesols' ?",
                "option_a": "Monet",
                "option_b": "Renoir",
                "option_c": "Van Gogh",
                "option_d": "Cézanne",
                "correct_option": "C"
            },
            {
                "question_text": "L'impressionnisme est né au :",
                "option_a": "18ème siècle",
                "option_b": "19ème siècle",
                "option_c": "20ème siècle",
                "option_d": "21ème siècle",
                "correct_option": "B"
            },
            {
                "question_text": "Pablo Picasso est associé à quel mouvement ?",
                "option_a": "Impressionnisme",
                "option_b": "Surréalisme",
                "option_c": "Cubisme",
                "option_d": "Romantisme",
                "correct_option": "C"
            }
        ]
    },
    
    # ============== PHILOSOPHY ==============
    {
        "title": "🤔 Philosophie - Les Grands Penseurs",
        "subject": "philosophy",
        "level_required": 2,
        "questions": [
            {
                "question_text": "Qui a dit 'Je pense, donc je suis' ?",
                "option_a": "Platon",
                "option_b": "Aristote",
                "option_c": "Descartes",
                "option_d": "Kant",
                "correct_option": "C"
            },
            {
                "question_text": "Socrate était le maître de :",
                "option_a": "Aristote",
                "option_b": "Platon",
                "option_c": "Épicure",
                "option_d": "Diogène",
                "correct_option": "B"
            },
            {
                "question_text": "Qui a écrit 'Le Contrat Social' ?",
                "option_a": "Voltaire",
                "option_b": "Montesquieu",
                "option_c": "Rousseau",
                "option_d": "Diderot",
                "correct_option": "C"
            },
            {
                "question_text": "L'existentialisme est associé à :",
                "option_a": "Nietzsche",
                "option_b": "Sartre",
                "option_c": "Marx",
                "option_d": "Hegel",
                "correct_option": "B"
            },
            {
                "question_text": "Qui a écrit 'Ainsi parlait Zarathoustra' ?",
                "option_a": "Schopenhauer",
                "option_b": "Heidegger",
                "option_c": "Nietzsche",
                "option_d": "Kierkegaard",
                "correct_option": "C"
            }
        ]
    },
    
    # ============== ECONOMICS ==============
    {
        "title": "💰 Économie - Les bases",
        "subject": "economics",
        "level_required": 2,
        "questions": [
            {
                "question_text": "Que signifie PIB ?",
                "option_a": "Produit Intérieur Brut",
                "option_b": "Prix International des Biens",
                "option_c": "Production Industrielle de Base",
                "option_d": "Profit Interne Bancaire",
                "correct_option": "A"
            },
            {
                "question_text": "L'inflation est :",
                "option_a": "Une baisse des prix",
                "option_b": "Une hausse générale des prix",
                "option_c": "Une baisse du chômage",
                "option_d": "Une hausse des salaires",
                "correct_option": "B"
            },
            {
                "question_text": "Qui a écrit 'La Richesse des Nations' ?",
                "option_a": "Karl Marx",
                "option_b": "John Keynes",
                "option_c": "Adam Smith",
                "option_d": "Milton Friedman",
                "correct_option": "C"
            },
            {
                "question_text": "La loi de l'offre et la demande dit que :",
                "option_a": "Si l'offre augmente, le prix augmente",
                "option_b": "Si la demande augmente, le prix augmente",
                "option_c": "Le prix est toujours fixe",
                "option_d": "L'offre égale toujours la demande",
                "correct_option": "B"
            },
            {
                "question_text": "Quelle institution européenne gère l'euro ?",
                "option_a": "Le FMI",
                "option_b": "La Banque Mondiale",
                "option_c": "La BCE",
                "option_d": "L'ONU",
                "correct_option": "C"
            }
        ]
    }
]

# Demo users for leaderboard
DEMO_USERS = [
    {"username": "MathGenius", "email": "math@demo.com", "level": 5, "score": 2500, "streak": 12, "avatar": "🧮"},
    {"username": "ScienceKid", "email": "science@demo.com", "level": 4, "score": 1800, "streak": 8, "avatar": "🔬"},
    {"username": "HistoryBuff", "email": "history@demo.com", "level": 4, "score": 1650, "streak": 15, "avatar": "📜"},
    {"username": "CodeMaster", "email": "code@demo.com", "level": 3, "score": 1200, "streak": 5, "avatar": "💻"},
    {"username": "LinguaPro", "email": "lingua@demo.com", "level": 3, "score": 1100, "streak": 7, "avatar": "📖"},
    {"username": "GeoExplorer", "email": "geo@demo.com", "level": 2, "score": 800, "streak": 4, "avatar": "🌍"},
    {"username": "ArtLover", "email": "art@demo.com", "level": 2, "score": 650, "streak": 3, "avatar": "🎨"},
    {"username": "MusicFan", "email": "music@demo.com", "level": 2, "score": 550, "streak": 6, "avatar": "🎵"},
    {"username": "SportsStar", "email": "sports@demo.com", "level": 1, "score": 300, "streak": 2, "avatar": "⚽"},
    {"username": "PhiloThinker", "email": "philo@demo.com", "level": 1, "score": 250, "streak": 1, "avatar": "🤔"},
]


def seed_database(db, Quiz, Question):
    """Seed the database with sample quizzes and demo users"""
    from models import User
    import bcrypt
    
    # Check if already seeded
    if Quiz.query.first():
        print("Database already seeded!")
        return
    
    # Seed demo users first
    for user_data in DEMO_USERS:
        password_hash = bcrypt.hashpw("demo123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user = User(
            username=user_data["username"],
            email=user_data["email"],
            password_hash=password_hash,
            level=user_data["level"],
            score=user_data["score"],
            streak=user_data["streak"],
            avatar=user_data["avatar"]
        )
        db.session.add(user)
    
    print(f"✅ Seeded {len(DEMO_USERS)} demo users!")
    
    # Seed quizzes
    for quiz_data in SAMPLE_QUIZZES:
        quiz = Quiz(
            title=quiz_data["title"],
            subject=quiz_data["subject"],
            level_required=quiz_data["level_required"]
        )
        db.session.add(quiz)
        db.session.flush()  # Get quiz.id
        
        for q_data in quiz_data["questions"]:
            question = Question(
                quiz_id=quiz.id,
                question_text=q_data["question_text"],
                option_a=q_data["option_a"],
                option_b=q_data["option_b"],
                option_c=q_data["option_c"],
                option_d=q_data["option_d"],
                correct_option=q_data["correct_option"]
            )
            db.session.add(question)
    
    db.session.commit()
    print(f"✅ Seeded {len(SAMPLE_QUIZZES)} quizzes!")
