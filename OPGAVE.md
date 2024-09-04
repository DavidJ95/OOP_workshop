# Lav denne mappe til et kodeprojekt

Mappen indeholder kode men den mangler adskillige ting for at være et komplet kodeprojekt

<details>
  <summary>Svar</summary>

  #### Tilføj:
  * README.md
  * requirements.txt
  * mk_env.sh
  * .venv/
  * .vscode/launch.json
  
</details>


# Fælles gennemgang i training-filerne
Gennemgå funktioner og objekter i plenum...


# Undersøg boldeksperimentet
Projektet src/dropkick/ undersøger hvad der sker når man slipper en bold i 2 sek
og sparker den lodret opad.

Scriptet køres af scripts/main_ball_functions.py og importerer calc_ball_kinematics.py.

1. Er scriptet pænt og let forståeligt?

2. Er underliggende funktioner pæne og let forståelige?

3. Er det tydeligt hvad underliggende funktioner gør og er de lette at teste?

4. Er de underliggende funktioner genbrugelige?


# Undersøg main_ball_object.py
Dette script forsøger at køre samme eksperiment med et bold-objekt

1. Er scriptet pænere?

2. Er det også lette at forstå?


# Skab en klasse som tilsvarer det objekt, scriptet forsøger at benytte sig af.
Kan objektet src/mass_object.py bruges/genbruges?
I så fald, mangler klassedefinitionen noget?

Tjek at resultatet er det samme som i main_ball_functions.py

1. Er objektet let at forstå?

2. Er objektet nemmere eller sværere at teste end funktionerne?

3. Er objektet genbrugeligt?

<details>
  <summary>Ekstra spørgsmål</summary>
  4. Er bagvedliggende objekt genbrugeligt?
</details>


<details>
  <summary>Eksempelløsning</summary>

  ### Tilføj til MassObject:


        def _update_momentum(self, duration_s):
            self.momentum = self.momentum + self.force * duration_s

        def _update_speed(self, duration_s):
            self.speed = self.speed + self.acceleration * duration_s

        def null_force(self):
            self.force = 0
            self.acceleration = 0
 

  ### BallObject:


    import mass_object

    class Ball(mass_object.MassObject):

        def __init__(self, mass_kg, speed_ms = 0, acceleration_ms2 = 0):
            super().__init__(mass_kg, speed_ms, acceleration_ms2)

        def drop(self, drop_duration_s):
            ''' Method that simulates a ball being held and dropped. '''

            self.null_force()

            print("Dropping ball...")
            self.apply_gravity(duration_s = drop_duration_s)

        def kick(self, force_N):
            ''' Method that simulates a ball being kicked. '''

            print("Kicking ball...")
            self.apply_force(force_N = force_N, duration_s = 0.08)
            self.null_force()
            self.apply_gravity()


</details>


