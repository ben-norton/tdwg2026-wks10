# fr_mineral_names_02_filtered filter report
> 2026-09-29 16:16:55

## Provenance
- Script: `src/transform/filter_by_exclusion_list.py`
- Command: `python src/transform/filter_by_exclusion_list.py --exclusion-list fr_mineral_names_exclusion_list.csv --input data/output/fr_mineral_names/fr_mineral_names_01.csv`
- Specification: `docs/transformations/de_mineral_names_transformations.md`
- Input: `data/output/fr_mineral_names/fr_mineral_names_01.csv`
- Exclusion list: `src/config/fr_mineral_names_exclusion_list.csv` (89 values)
- Single exclusions: `data/output/fr_mineral_names/single_exclusions.csv` (70 values)
- Output: `data/output/fr_mineral_names/fr_mineral_names_02_filtered.csv`
- Time elapsed: 0.021 s
- Python 3.14.4, pandas 3.0.3

## Description
Removed rows whose `fr_mineral_name` value, trimmed, exactly matches a full-value exclusion or a value in single_exclusions.csv. Then deleted each substring exclusion from the remaining values, in list order, and dropped rows left empty. Finally dropped duplicate values (case-insensitive, first occurrence kept). No other change is made to values.

## Statistics
| | input | output |
|---|---:|---:|
| Records | 3653 | 3407 |
| Columns | 1 | 1 |
| Unique values | 3652 | 3407 |
| Empty values | 0 | 0 |
| Duplicate values | 1 | 0 |

- Records removed: 89
- Records removed by single exclusions only: 0
- Exclusion values with no match in the input: 0
- Values changed by substring exclusions: 563
- Records dropped because substring exclusions left them empty: 0
- Duplicate records dropped after exclusion: 157

## Removed values
- (Carbonate-)cyanotrichite
- > 10 Éch. Cassiterite, Etc. (Liste)
- > 10 Éch. Magnétite, Grenat, Scheelite
- > 20 Éch. Recherche Agardite-Ce, Etc. (Liste)
- > 5 Éch. Magnetite, Etc.
- A analyser
- à identifier
- Acétate de Cu
- Acétate de Cu et Ca
- Acétate de Cu et Sr
- Alurgite = Mg, Fe, Mn Muscovite
- Amalgame [pas une espèce]
- Amazonite = Microcline
- Amber (2 Éch.)
- Amianthus=Tremolite, Actinolite, Chrysotile, etc
- Analcime (-1c,-1q,-1o,-1m)
- Argent (-3c,-2h,-4h)
- Argent (-3c,-2h,-4h) 'Amalgam'
- Argent (-3c,-2h,-4h) 'Kongsbergite'
- Formiate de Ca
- Formiate de Cd
- Inconnu
- Oxalate de K
- Sulfate d'Al et Cr
- Sulfate d'Al et de Tl
- Sulfate d'Al et K
- Sulfate d'Al et NH4
- Sulfate d'Al et Tl
- Sulfate d'Al, Cr et NH4
- Sulfate d'in et Cs
- Sulfate de Ca
- Sulfate de Cd
- Sulfate de Co
- Sulfate de Co et de Tl
- Sulfate de Co et K
- Sulfate de Co et NH4
- Sulfate de Cr et de NH4
- Sulfate de Cr et K
- Sulfate de Cr, Al et Rb
- Sulfate de Cs et Al
- Sulfate de Cs et de Cr
- Sulfate de Cu
- Sulfate de Cu et Cr
- Sulfate de K
- Sulfate de K Et Al
- Sulfate de K et Al hydraté
- Sulfate de K et Cr
- Sulfate de K et Cr hydraté
- Sulfate de K et d'Al
- Sulfate de K et Li
- Sulfate de K, Cr et NH4
- Sulfate de K, Fe et Cr
- Sulfate de Mg
- Sulfate de Mg et K
- Sulfate de N
- Sulfate de NH4
- Sulfate de NH4 et d'Al
- Sulfate de NH4 et de Cu
- Sulfate de NH4 et de Fe
- Sulfate de NH4 et de Zn
- Sulfate de NH4 et Fe
- Sulfate de NH4 et K
- Sulfate de Ni
- Sulfate de Ni et K
- Sulfate de Ni et NH4
- Sulfate de Ni et Rb
- Sulfate de Ni hydraté
- Sulfate de Ni, Cr et NH4
- Sulfate de Rb et In
- Sulfate de Tl et Cr
- Sulfate de Tl et de Cr
- Sulfate de Tl, Cr et Al
- Sulfate de Zn et K
- Sulfate de Zn et NH4
- Sulfate hydraté de Co,Cu,Zn,Mg,K
- Sulfate hydraté de Fe et NH4
- Sulfate hydraté de Mg et NH4
- Sulfate hydraté de Ni,Cu,Co,Zn
- Sulfate hydraté de Ni,Mg
- Sulfite de Sr
- Sulfure de Cd
- Sulfure de Na
- Tartrate de K
- Tartrate de K et Na
- The Storr, Skye, Scotland, Uk
- Tungstenite (-2h,-3r)
- Urate de K
- Us Gypsum Mine, Empire, Nv
- vert clair

## Substring exclusions (applied in this order)
| pattern | values affected |
|---|---:|
| `\s+=\s.*$` | 399 |
| `\s+de\s.*$` | 104 |
| `(?i)\s*\bsynth[ée]tique\b` | 2 |
| `\s*\(\s*\?+\s*\)|\s*\?+` | 58 |

## Values changed by substring exclusions
| before | after |
|---|---|
| Acmite = Aegirine | Acmite |
| Actinolite-tremolite? | Actinolite-tremolite |
| Adulaire = Orthoclase | Adulaire |
| Adulare = Orthoclase | Adulare |
| Adularia = Orthoclase | Adularia |
| Agricolite = Eulytite | Agricolite |
| Aiguemarine (Aigue-Marine) = Aquamarin = Beryl | Aiguemarine (Aigue-Marine) |
| Alabaster = Gypsum | Alabaster |
| Alkali Feldspars = Feldspars With K+ And Na+ | Alkali Feldspars |
| Allevardite = Rectorite | Allevardite |
| Almandite = Almandine | Almandite |
| Alun de potassium | Alun |
| Amosite = Mainly Grunerite | Amosite |
| Amphibole = Amphibole Group | Amphibole |
| Analcite = Analcime | Analcite |
| Antigorite-chrysotile? | Antigorite-chrysotile |
| Antimoniate de Pb | Antimoniate |
| Apatite = Groupe | Apatite |
| Apatite-(Cacl) = Chlorapatite | Apatite-(Cacl) |
| Apatite-(Caf) = Fluorapatite | Apatite-(Caf) |
| Apatite-(Caoh) = Hydroxylpatite | Apatite-(Caoh) |
| Aphanese = Clinoclase | Aphanese |
| Apophyllite = Grp. | Apophyllite |
| Apophyllite ? | Apophyllite |
| Aquamarine = Beryl | Aquamarine |
| Argent Des Chats = Muscovite | Argent Des Chats |
| Argentite = Argyrose | Argentite |
| Arseniate de K | Arseniate |
| Arséniate de K | Arséniate |
| Arséniate de Na | Arséniate |
| Arséniate de NH4 | Arséniate |
| Arseniosiderite? | Arseniosiderite |
| Arsénite de Cu | Arsénite |
| Asbeste? | Asbeste |
| Ascharite = Szaibelyite | Ascharite |
| Axinite = Axinite-(Fe) Or -(Mg) Or -(Mn) | Axinite |
| Baikalite = Diopside | Baikalite |
| Bakerite = Datolite | Bakerite |
| Barbertonite = Stichtite | Barbertonite |
| Bariopyrochlore = Zero-Valent-Dominant Pyrochlore | Bariopyrochlore |
| Barite = Baryte | Barite |
| Barium Pharmacosiderite = Bariopharmacosiderite | Barium Pharmacosiderite |
| Barkevikite = Ferrohornblende | Barkevikite |
| Barrotite à revérifier? | Barrotite à revérifier |
| Barytine = Barite | Barytine |
| Barytine = Baryte | Barytine |
| Basaluminite = Felsobanyaite | Basaluminite |
| Bastinite = Hureaulite | Bastinite |
| Bastnaesite-(Ce) = Bastnasite-(Ce) | Bastnaesite-(Ce) |
| Bastonite = Biotite | Bastonite |
| Bauxite = Hydroxides And Oxides Of Al And Fe | Bauxite |
| Bayankhanite (?) | Bayankhanite |
| Bernstein = Amber | Bernstein |
| Beryl synthétique | Beryl |
| Béryl synthétique | Béryl |
| Betpakdalite = Betpakdalite-Caca | Betpakdalite |
| Bindheimite = Oxyplumboromeite Or Plumboromeite | Bindheimite |
| Biotite (-1m,-2m,-5m1,-6a) = Series Name | Biotite (-1m,-2m,-5m1,-6a) |
| Bisbeeite = Plancheite-Chrysocolla (?) | Bisbeeite |
| Bloedite = Blodite | Bloedite |
| Bobdownsite = Whitlockite | Bobdownsite |
| Bolivarite = Evansite (?) | Bolivarite |
| Borate de Ba | Borate |
| Borate de Na | Borate |
| Boronatrocalcite = Ulexite | Boronatrocalcite |
| Brammallite = A Series Name | Brammallite |
| Brasilianite = Brazilianite | Brasilianite |
| Bromate de K | Bromate |
| Bromate de Na | Bromate |
| Bromure de Ba hydraté | Bromure |
| Bromure de K | Bromure |
| Bronzite = Ferroan Enstatite | Bronzite |
| Buergerite = Fluorbuergerite | Buergerite |
| Bursaite = Mixture Of Pb And Bi Sulfosalts | Bursaite |
| Byssolite = Actinolite-Tremolite | Byssolite |
| Cabrerite = Magnesian Annabergite | Cabrerite |
| Cacoxenite ??? | Cacoxenite |
| Calamine = Hemimorphite | Calamine |
| Calciovolborthite = Tangeite | Calciovolborthite |
| Calcite Cobaltoan = Calcite | Calcite Cobaltoan |
| Californite = Vesuvianite | Californite |
| Campylite = Phosphore Mimetite | Campylite |
| Carbonate Cyanotrichite = Carbonatecyanotrichite | Carbonate Cyanotrichite |
| Carbonate de Ca | Carbonate |
| Carbonate de Cu | Carbonate |
| Carbure de Si | Carbure |
| Carbure de silicium | Carbure |
| Catgold (Cat Gold) = Muscovite | Catgold (Cat Gold) |
| Celestite = Celestine | Celestite |
| Centrallasite = Gyrolite | Centrallasite |
| Chalcolite = Torbernite | Chalcolite |
| Chalybite = Siderite | Chalybite |
| Cheralite-(Ce) = Monazite-(Ce) | Cheralite-(Ce) |
| Chessylite = Azurite | Chessylite |
| Chiastolite = Andalusite | Chiastolite |
| Chlorate de Ba | Chlorate |
| Chlorate de Cu et K | Chlorate |
| Chlorate de Cu et NH4 | Chlorate |
| Chlorate de Mn | Chlorate |
| Chlorate de Na | Chlorate |
| Chlorate de Na et K | Chlorate |
| Chlorate de Sn et NH4 | Chlorate |
| Chlorite = Chlorite Group | Chlorite |
| Chlorite = GRP. | Chlorite |
| Chloro-Fluorure de Ba | Chloro-Fluorure |
| Chloro-fluorure de Ca et Y | Chloro-fluorure |
| Chloro-Fluorure de Sr | Chloro-Fluorure |
| Chloromelanite = Jadeite | Chloromelanite |
| Chlorure de Ba et Cd | Chlorure |
| Chlorure de K | Chlorure |
| Chlorure de K et Pt | Chlorure |
| Chlorure de Pt | Chlorure |
| Chromate de K | Chromate |
| Chromate de Mg et NH4 | Chromate |
| Chromate de NH4 | Chromate |
| Cleavelandite = Albite | Cleavelandite |
| Clinochlore Manganoan = Clinochlore | Clinochlore Manganoan |
| Clinohydroxylapatite = Hydroxylapatite-M | Clinohydroxylapatite |
| Clinopyroxene = Series In Pyroxene Group | Clinopyroxene |
| Clinostrengite = Phosphosiderite | Clinostrengite |
| Clinotirolite = Clinotyrolite = Tangdanite | Clinotirolite |
| Clinotyrolite = Tangdanite | Clinotyrolite |
| Cobaltoadamite = Adamite | Cobaltoadamite |
| Cobaltocalcite = Sphaerocobaltite | Cobaltocalcite |
| Coeruleolactite = Cuprian Planerite + Crandallite | Coeruleolactite |
| Collophane = Collophanite = Carbonate Apatite | Collophane |
| Collophanite = Carbonate Apatite | Collophanite |
| Columbite-tantalite (?) | Columbite-tantalite |
| Comptonite = Thomsonite | Comptonite |
| Copperas = Melanterite | Copperas |
| Crocidolite = Riebeckite | Crocidolite |
| Crossite = Glaucophane Or Riebeckite | Crossite |
| Crucite = Chiastolite = Andalusite | Crucite |
| Cuivre Arseniate = Olivenite Or Chalcophyllite | Cuivre Arseniate |
| Cuivre Carbonate Bleu = Azurite | Cuivre Carbonate Bleu |
| Cuivre Hydrosiliceux = Chrysocolla | Cuivre Hydrosiliceux |
| Cuivre Phosphate = Libethenite Or Pseudomalachite | Cuivre Phosphate |
| Cuivre Veloute = Cyanotrichite | Cuivre Veloute |
| Cuprian Austinite = Austinite | Cuprian Austinite |
| Cuproadamite = Adamite | Cuproadamite |
| Cuprodescloizite = Mottramite | Cuprodescloizite |
| Cuprofaustite = Faustite | Cuprofaustite |
| Cuprotungstite ?? | Cuprotungstite |
| Cyanite = Kyanite | Cyanite |
| Cyanose = Chalcanthite | Cyanose |
| Cyanure de Co et K | Cyanure |
| Cyanure de Fe et K | Cyanure |
| Cyanure de Mg et Pt | Cyanure |
| Cyanure de Pt et Er | Cyanure |
| Cyanure de Pt et Mg | Cyanure |
| Cyrtolite = Zircon | Cyrtolite |
| Dahllite = Hydroxylapatite Carbonate Rich | Dahllite |
| Damourite = Muscovite | Damourite |
| Dannemorite = Manganogrunerite | Dannemorite |
| Dannemorite DISC??? | Dannemorite DISC |
| Demantoide = Andradite | Demantoide |
| Dendrites de Mn | Dendrites |
| Descloizite? | Descloizite |
| Desmine = Stilbite | Desmine |
| Destinezite = Diadochite | Destinezite |
| Devillite = Devilline | Devillite |
| Deweylite = Clinochrysotile-Lizardite (?) | Deweylite |
| Diallage = Diopside | Diallage |
| Dialogite = Rhodochrosite | Dialogite |
| Dichroite = Cordierite | Dichroite |
| Dichromate de K | Dichromate |
| Diomignite = Zabuyelite | Diomignite |
| Dipyre = Scapolite | Dipyre |
| Disthene = Kyanite | Disthene |
| Dithionate de Ba | Dithionate |
| Dithionate de K | Dithionate |
| Dithionate de Na | Dithionate |
| Dithioniate de Na | Dithioniate |
| Doverite = Synchysite-(Y) | Doverite |
| Dubuissonite = Montmorillonite | Dubuissonite |
| Duhamelite = Mottramite Bismuthian | Duhamelite |
| Eisenspat = Siderite | Eisenspat |
| Ekmaniteespèce ? | Ekmaniteespèce |
| Emerald = Beryl | Emerald |
| Emeraude = Emerald = Beryl | Emeraude |
| Endlichite = Arsenatian Vanadinite | Endlichite |
| Enigmatite = Aenigmatite | Enigmatite |
| Epidesmine = Stilbite | Epidesmine |
| Errite = Parsettensite | Errite |
| Esmeralda = Emerald = Beryl | Esmeralda |
| Eucolite = Eudialyte | Eucolite |
| Eulytite = Eulytine | Eulytite |
| Evenkite (?) | Evenkite |
| Falkmanite = Boulangérite | Falkmanite |
| Fassaite = Diopside Or Augite | Fassaite |
| Fauserite = Epsomite Mn | Fauserite |
| Feldspar = Feldspar Group | Feldspar |
| Feldspath = Feldspar Group | Feldspath |
| Fer Arseniate = Pharmacosiderite | Fer Arseniate |
| Fer Azure = Vivianite | Fer Azure |
| Fer Carbonate = Siderite | Fer Carbonate |
| Fer Phosphate = Vivianite | Fer Phosphate |
| Ferriannite (Ferri-Annite) = Tetraferriannite | Ferriannite (Ferri-Annite) |
| Ferriberaunite = Eleonorite | Ferriberaunite |
| Ferricyanure de K | Ferricyanure |
| Ferro-Axinite = Axinite-(Fe) | Ferro-Axinite |
| Ferroaxinite = Axinite-(Fe) | Ferroaxinite |
| Ferrocyanure de Fe | Ferrocyanure |
| Ferrocyanure de K | Ferrocyanure |
| Ferroschallerite = Nelenite | Ferroschallerite |
| Fibrolite = Sillimanite | Fibrolite |
| Flos Ferri = Aragonite | Flos Ferri |
| Fluorapophyllite = Apophyllite-(Kf) | Fluorapophyllite |
| Fluorite recouvert de Quartz | Fluorite recouvert |
| Fluorure de Ba | Fluorure |
| Fluorure de Ba et Eu | Fluorure |
| Fluorure de Ba et Mg | Fluorure |
| Fluorure de Ba et Sm | Fluorure |
| Fluorure de Ca | Fluorure |
| Fluorure de Ca et Ag | Fluorure |
| Fluorure de Ca et Cr | Fluorure |
| Fluorure de Ca et Eu | Fluorure |
| Fluorure de Ca et Ho | Fluorure |
| Fluorure de Ca et Sc | Fluorure |
| Fluorure de Ca et Sm | Fluorure |
| Fluorure de Ca et Tm | Fluorure |
| Fluorure de Ca et Y | Fluorure |
| Fluorure de Ca et Yb | Fluorure |
| Fluorure de Ca. Yb et Ho | Fluorure |
| Fluorure de Li | Fluorure |
| Fluorure de Sm et Ba | Fluorure |
| Fluorure de Sr | Fluorure |
| Fluorure de Sr et Ag | Fluorure |
| Fluorure de Sr et Er | Fluorure |
| Fluorure de Sr et Eu | Fluorure |
| Fluorure de Sr et Pr | Fluorure |
| Fluorure de Sr et Sm | Fluorure |
| Fluorure de Sr et Tm | Fluorure |
| Fowlerite = Zincian Rhodonite | Fowlerite |
| Francolite = Carbonatefluorapatite | Francolite |
| Fraueneis = Gypsum | Fraueneis |
| Frauenglas = Mica | Frauenglas |
| Frauenglas = Muscovite | Frauenglas |
| Fuchsite = Chromian Muscovite | Fuchsite |
| Gainesite-(Nana) = Gainesite | Gainesite-(Nana) |
| Garnet = Garnet Supergroup | Garnet |
| Garniérite DISC??? | Garniérite DISC |
| Geneveite = Theisite (?) | Geneveite |
| Gesso = Gypsum | Gesso |
| Giobertite = Magnesite | Giobertite |
| Gips = Gypsum | Gips |
| Glagerite = Halloysite | Glagerite |
| Glaserite = Aphthitalite | Glaserite |
| Glaucolite = Glaukolite | Glaucolite |
| Glaucosphaerite = Glaukosphaerite | Glaucosphaerite |
| Glaukolite = Scapolite = Meionite-Marialite | Glaukolite |
| Glimmer = Mica | Glimmer |
| Godovikovite ? | Godovikovite |
| Grammatite = Tremolite | Grammatite |
| Gregoryite ? | Gregoryite |
| Griffithite = Ferroan Saponite | Griffithite |
| Gruenlingite DISC??? | Gruenlingite DISC |
| Grunlingite = Mixture Joseite + Bismuthinite | Grunlingite |
| Gypse = Gypsum | Gypse |
| Haarsalz = Halotrichite | Haarsalz |
| Herrengrundite = Devilline | Herrengrundite |
| Herschelite = Chabazite-Na | Herschelite |
| Herschelite DISC??? | Herschelite DISC |
| Hessonite = Grossular | Hessonite |
| Hexagonite = Manganoan Tremolite | Hexagonite |
| Hibschite = Grossular Hydroxyl Variety | Hibschite |
| Hidalgoite (arsenogorceixite?) | Hidalgoite (arsenogorceixite) |
| Hiddenite = Spodumene | Hiddenite |
| Higginsite = Conichalcite | Higginsite |
| Hoernesite = Hornesite | Hoernesite |
| Hornblende = Ferrohornblende, Magnesiohornblende | Hornblende |
| Huréaulite = Hureaulite | Huréaulite |
| Hyaloallophane = Allophane + Hyalite | Hyaloallophane |
| Hydro Ugrandite = Hydrougrandite (Discredited) | Hydro Ugrandite |
| Hydrogrossular = Hibschite-Katoite | Hydrogrossular |
| Hydromuscovite = Illite | Hydromuscovite |
| Hydronium Jarosite = Hydroniumjarosite | Hydronium Jarosite |
| Hydrougrandite = Discredited | Hydrougrandite |
| Hydroxy-sulfate de Zn | Hydroxy-sulfate |
| Hydroxyapatite = Hydroxylpatite | Hydroxyapatite |
| Hydroxyl-Herderite = Hydroxylherderite | Hydroxyl-Herderite |
| Hydroxylapatite-M = Hydroxylapatite | Hydroxylapatite-M |
| Hypersthene = Enstatite-Ferrosilite | Hypersthene |
| Idocrase = Vesuvianite | Idocrase |
| Iidateite (?) | Iidateite |
| Illite = A Series Name | Illite |
| Illite[pas une espèce] = groupe | Illite[pas une espèce] |
| Imogolite (?) | Imogolite |
| Iodure de Hg | Iodure |
| Iodure de K | Iodure |
| Iolite = Cordierite | Iolite |
| Iriginite ??? | Iriginite |
| Iron Cordierite = Sekaninaite | Iron Cordierite |
| Jade (?) | Jade |
| Jais = Jet (Gemstone From Hard Black Lignite) | Jais |
| Jefferisite = Vermiculite | Jefferisite |
| Joaquinite = Joaquinite Group | Joaquinite |
| Kalipyrochlore = Hydropyrochlore | Kalipyrochlore |
| Kalkeisengranat = Andradite | Kalkeisengranat |
| Kalkgranat = Andradite | Kalkgranat |
| Kalkspat = Calcite | Kalkspat |
| Kamacite = Ni Rich Fe In Meteorite | Kamacite |
| Kammererite = Chromian Clinochlore | Kammererite |
| Kaolinite-Smectite = Clay Minerals | Kaolinite-Smectite |
| Keilhauite = Yttrian Titanite | Keilhauite |
| Klipsteinite = Altered Rhodonite | Klipsteinite |
| Knipovichite = Chromian Alumohydrocalcite | Knipovichite |
| Kobaltbluthe = Erythrite | Kobaltbluthe |
| Koettigite = Kottigite | Koettigite |
| Kolwézite = Kolwezite | Kolwézite |
| Kramerite = Probertite | Kramerite |
| Krausite ?? | Krausite |
| Kroehnkite = Krohnkite | Kroehnkite |
| Kröhnkite? | Kröhnkite |
| Ktenasite Cobaltoan Nickeloan = Ktenasite | Ktenasite Cobaltoan Nickeloan |
| Kunzite = Spodumene | Kunzite |
| Kupferglimmer = Chalcophyllite | Kupferglimmer |
| Kupfergrun = Chrysocolla | Kupfergrun |
| Kupferlasur = Azurite | Kupferlasur |
| Kupferschaum = Tyrolite | Kupferschaum |
| Kupfervitriol = Chalcanthite | Kupfervitriol |
| Kutnahorite = Kutnohorite | Kutnahorite |
| Lapis Lazuli = Lazurite | Lapis Lazuli |
| Laubmannite =  Dufrenite, Kidwellite, Beraunite | Laubmannite |
| Lavrovite = Diopside | Lavrovite |
| Leitite? | Leitite |
| Lepidolite = Trilithionite | Lepidolite |
| Lepidomelane = Ferrian Biotite | Lepidomelane |
| Lesserite = Inderite | Lesserite |
| Lettsomite = Cyanotrichite | Lettsomite |
| Leuchtenbergite = Clinochlore | Leuchtenbergite |
| Leucochalcite = Olivenite | Leucochalcite |
| Levynite = Levyne | Levynite |
| Lievrite = Ilvaite | Lievrite |
| Linnaeite(?) | Linnaeite |
| Litidionite = Lithidionite | Litidionite |
| Lusungite = Benauite | Lusungite |
| Lyellite = Devilline | Lyellite |
| Mackintoshite = Thorogummite | Mackintoshite |
| Magnesio-gedrite DISC??? | Magnesio-gedrite DISC |
| Magnesioanthophyllite = Anthophyllite | Magnesioanthophyllite |
| Magnesiocummingtonite = Cummingtonite | Magnesiocummingtonite |
| Magnesium Astrophyllite = Lobanovite | Magnesium Astrophyllite |
| Magnesiumastrophyllite = Lobanovite | Magnesiumastrophyllite |
| Mahlmoodite = Malhmoodite | Mahlmoodite |
| Malacon = Zircon | Malacon |
| Malaquita = Malachite | Malaquita |
| Manasseite = Hydrotalcite | Manasseite |
| Manganaxinite = Axinite-(Mn) | Manganaxinite |
| Manganocalcite = Calcite | Manganocalcite |
| Manganomelane = Mn Oxides | Manganomelane |
| Manganophyllite = Manganoan Biotite | Manganophyllite |
| Mantiennéite = Mantienneite | Mantiennéite |
| Marble = Often Calcite | Marble |
| Marienglas = Muscovite Or Gypsum | Marienglas |
| Mariposite = Chromian Phengite = Muscovite | Mariposite |
| Mayenite = Chlormayenite | Mayenite |
| Melanite = Titanian Andradite | Melanite |
| Melinophane = Meliphanite | Melinophane |
| Melinose = Wulfenite | Melinose |
| Meliphanite DISC? | Meliphanite DISC |
| Mendozavilite = Mendozavilite-Nafe | Mendozavilite |
| Menilite = Opal | Menilite |
| Meroxene = Biotite | Meroxene |
| Meta Aluminite = Meta-Aluminite | Meta Aluminite |
| Meta Alunogen = Meta-Alunogen | Meta Alunogen |
| Metastrengite = Phosphosiderite | Metastrengite |
| Meurigite = Meurigite-K | Meurigite |
| Mica = Mica Group | Mica |
| Mimetese = Mimetite | Mimetese |
| Mizzonite = Marialite-Meionite | Mizzonite |
| Monazite-(Ce?) | Monazite-(Ce) |
| Monheimite = Smithsonite | Monheimite |
| Monsmedite = Voltaite | Monsmedite |
| Mosandrite = Rinkite altéré | Mosandrite |
| muscovite? | muscovite |
| Natrolite? | Natrolite |
| Natrolite? aragonite? | Natrolite aragonite |
| Nephrite = Actinolite | Nephrite |
| Nepouite ??? | Nepouite |
| Niobate de Cr et Li | Niobate |
| Nitrate de Ba | Nitrate |
| Nitrate de Pb | Nitrate |
| Nitrate de Sr | Nitrate |
| Nitre = Niter | Nitre |
| Nitrokalit = Niter | Nitrokalit |
| Nitronatrite = Nitratine | Nitronatrite |
| Nocerite = Fluoborite | Nocerite |
| Oeil de faucon | Oeil |
| Oeil de tigre | Oeil |
| Oellacherite = Barian Muscovite | Oellacherite |
| Olivine = Fayalite-Forsterite Or Olivine Group | Olivine |
| Opalsinter = Stilolite | Opalsinter |
| Or Des Chats = Muscovite | Or Des Chats |
| Orpheite = Hinsdalite | Orpheite |
| Orthite = Allanite-(Ce) | Orthite |
| Orthochrysotile = Chrysotile | Orthochrysotile |
| Orthopyroxene = Series In Pyroxene Group | Orthopyroxene |
| Orthose = Orthoclase | Orthose |
| Ouro Preto = Oxygenated Pt, Pd, Au, Cu, Fe, Mn | Ouro Preto |
| Oxiberaunite = Eleonorite | Oxiberaunite |
| Oxyde de Bi, Sr, Ca et Cu | Oxyde |
| Oxyde de Ce et Pr | Oxyde |
| Oxyde de La et Dy | Oxyde |
| Oxyde de La et Tm | Oxyde |
| Oxyde de La, Zr et Er | Oxyde |
| Oxyde de Nd | Oxyde |
| Oxyde de Sm et Zr | Oxyde |
| Palladinite (?) | Palladinite |
| Palygorskite? | Palygorskite |
| Pandermite = Priceite | Pandermite |
| Paramelaconite (?) | Paramelaconite |
| Parawollastonite = Wollastonite-2m | Parawollastonite |
| Peisleyite ?? | Peisleyite |
| Pennine = Clinochlore | Pennine |
| Penninite = Clinochlore | Penninite |
| Pericline = Albite | Pericline |
| Peridot = Forsterite | Peridot |
| Peristerite = Albite | Peristerite |
| Pharmacolite ? | Pharmacolite |
| Phenacite = Phenakite | Phenacite |
| Phengite = A Series Name | Phengite |
| Phosphate de K | Phosphate |
| Phosphate de NH4 | Phosphate |
| Phosphohedyphane-(F) = Fluorphosphohedyphane | Phosphohedyphane-(F) |
| Pinite = Altered Cordierite | Pinite |
| Pisekite = Monazite | Pisekite |
| Plagioclase = Feldspar Group | Plagioclase |
| Planchéite = Plancheite | Planchéite |
| Plessite = Kamacite-Taenite | Plessite |
| Plomb Carbonate Rhomboidal = Leadhillite | Plomb Carbonate Rhomboidal |
| Potstone = Talc | Potstone |
| Prixite = Mimetite | Prixite |
| Produits de Geyser | Produits |
| Ptilolite = Mordenite | Ptilolite |
| Pyropissite ? | Pyropissite |
| Pyroxene = Pyroxene Group | Pyroxene |
| Quercyite = Carbonate Apatite | Quercyite |
| Ralstonite = Hydrokenoralstonite | Ralstonite |
| Ramsayite = Lorenzenite | Ramsayite |
| Ripidolite = Ferroan Clinochlore | Ripidolite |
| Roemerite = Romerite | Roemerite |
| Roesslerite = Rosslerite | Roesslerite |
| Roselite Beta = Roselitebeta | Roselite Beta |
| Rostite = Khademite | Rostite |
| Rothbraunsteinerz = Rhodonite | Rothbraunsteinerz |
| Rother Eisen-Vitriol = Botryogen | Rother Eisen-Vitriol |
| Rothervitriol = Bieberite | Rothervitriol |
| Rothes Bleierz = Crocoite | Rothes Bleierz |
| Rothoffite = Andradite | Rothoffite |
| Rothspath = Rhodonite Or Rhodochrosite | Rothspath |
| Rothstein = Rhodonite Or Rhodochrosite | Rothstein |
| Rubellite = Elbaite | Rubellite |
| Salite = Sahlite = Diopside | Salite |
| Salpeter = Niter | Salpeter |
| Salpetre = Niter | Salpetre |
| Saussurite = Zoisite, Scapolite, Etc. | Saussurite |
| Scapolite = groupe | Scapolite |
| Scapolite = Marialite-Meionite | Scapolite |
| Schefferite = Manganoan Aegirine | Schefferite |
| Schmeiderite = Schmiederite | Schmeiderite |
| Schoenite = Picromerite | Schoenite |
| Schörl = Schorl | Schörl |
| Schroeckingerite = Schrockingerite | Schroeckingerite |
| Schweizerite = Serpentine | Schweizerite |
| Schwerspat = Baryte | Schwerspat |
| Séléniate de Cu | Séléniate |
| Séléniate de Ni et Ag | Séléniate |
| Selenite = Gypsum | Selenite |
| Sericite = Muscovite | Sericite |
| Serpentine = groupe | Serpentine |
| Serpentine = Serpentine Group | Serpentine |
| Shepardite (Of Rose) = Enstatite | Shepardite (Of Rose) |
| Silicofluorure de Co | Silicofluorure |
| Silicofluorure de Ni | Silicofluorure |
| Sillimanite (?) | Sillimanite |
| Smaragd = Emerald = Beryl | Smaragd |
| Smectite = Smectite Group | Smectite |
| Smeraldo = Emerald = Beryl | Smeraldo |
| Smithsonite Cobaltoan = Smithsonite | Smithsonite Cobaltoan |
| Soda Feldspar = Albite | Soda Feldspar |
| Soda Niter = Nitratine | Soda Niter |
| Spessartite = Spessartine | Spessartite |
| Sphene = Titanite | Sphene |
| Spherocobaltite = Sphaerocobaltite | Spherocobaltite |
| Spodiosite =  Fluorapatite, Calcite, Serpentine | Spodiosite |
| Stannate de Pb | Stannate |
| Staurotide = Staurolite | Staurotide |
| Steatite = Talc | Steatite |
| Stibnite/zinckenite avec stibiconite? | Stibnite/zinckenite avec stibiconite |
| Stilbite = Desmine | Stilbite |
| Stilbite ? | Stilbite |
| Straetlingite = Stratlingite | Straetlingite |
| Strahlstein = Actinolite | Strahlstein |
| Strontianite? | Strontianite |
| Strontiopiemontite = Piemontite-(Sr) | Strontiopiemontite |
| Sturtite = Hisingerite Or Neotocite | Sturtite |
| Succinite = Amber | Succinite |
| Synchisite-(Ce) = Synchysite-(Ce) | Synchisite-(Ce) |
| Synchisite-(Nd) = Synchysite-(Nd) | Synchisite-(Nd) |
| Synchisite-(Y) = Synchysite-(Y) | Synchisite-(Y) |
| Synchysite-(Y) ? ou (Ce) ou (Nd) | Synchysite-(Y) ou (Ce) ou (Nd) |
| Synchysite-(Y) ? ou (Ce) ou(Nd) | Synchysite-(Y) ou (Ce) ou(Nd) |
| Taeniolite = Tainiolite | Taeniolite |
| Tanzanite = Zoisite | Tanzanite |
| Taraspite = A Ni Rich Dolomite | Taraspite |
| Tarnowitzite = Plumboan Aragonite | Tarnowitzite |
| Tarnowskite = Tarnowitzite | Tarnowskite |
| Taylorite = Ammonian Arcanite | Taylorite |
| Tellurate de Cu | Tellurate |
| Tellurate de NH4 | Tellurate |
| Tetranatrolite = Gonnardite | Tetranatrolite |
| Tétranatrolite DISC ??? | Tétranatrolite DISC |
| Thiosulfate de Na | Thiosulfate |
| Thortveitite? | Thortveitite |
| Thulite = A Pink Zoisite Manganoan Variety | Thulite |
| Tincal = Borax | Tincal |
| Tirolite = Tyrolite | Tirolite |
| Tlalocite ?? faux? | Tlalocite faux |
| Tocornalite (?) | Tocornalite |
| Tocornalite DISC ??? | Tocornalite DISC |
| Topazolite = Andradite | Topazolite |
| Torbernite? | Torbernite |
| Tourmaline = Grp. | Tourmaline |
| Tourmaline = Tourmaline Group | Tourmaline |
| Triborate de Li | Triborate |
| Trichalcite = Tyrolite | Trichalcite |
| Trichlorite = Tyrolite | Trichlorite |
| Tungstate de Ca | Tungstate |
| Turnerite = Monazite | Turnerite |
| Uralite = Amphibole Pseudomorphous After Pyroxene | Uralite |
| Uranite (?) | Uranite |
| Uranite = Autunite And Meta-Autunite Groups | Uranite |
| Uranotile = Uranophane | Uranotile |
| Uranotile Beta = Uranophane Beta | Uranotile Beta |
| Ureyite = Kosmochlor | Ureyite |
| Urvolgyite = Devilline | Urvolgyite |
| Utahlite = Variscite | Utahlite |
| Uvite = A New Oxy-Tourmaline? | Uvite |
| Vanadate de Na | Vanadate |
| Vanadate de NH4 | Vanadate |
| Vanadiumdravite = Oxyvanadiumdravite | Vanadiumdravite |
| Varaite = Namansilite | Varaite |
| Varaite ?? | Varaite |
| Verdelite = Elbaite Or Schorl | Verdelite |
| Violan = Diopside | Violan |
| Volchonskoite = Volkonskoite | Volchonskoite |
| Wad = Massive Mangnese Oxides | Wad |
| Weinschenkite = Churchite-(Y) | Weinschenkite |
| Wernerite = Marialite-Meionite | Wernerite |
| Wilkeite = Apatite Or Fluorellestadite | Wilkeite |
| Willemite (?) | Willemite |
| Winstanleyite? | Winstanleyite |
| Woehlerite = Wohlerite | Woehlerite |
| Wollastonite-2m (?) | Wollastonite-2m |
| Yamatoite = Momoiite | Yamatoite |
| Yttroorthite (Yttro Orthite) = Allanite-(Y) | Yttroorthite (Yttro Orthite) |
| Yttrotitanite = Titanite | Yttrotitanite |
| Zincvoltaite = Zincovoltaite | Zincvoltaite |
| Zinkglaserz = Hemimorphite | Zinkglaserz |
| Zinkkieselerz = Hemimorphite | Zinkkieselerz |
| Zinkspat = Smithsonite | Zinkspat |
| Zinnwaldite = Siderophyllite-Polylithionite | Zinnwaldite |
