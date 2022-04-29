-- Opretter bruger tabel
create table if not exists Bruger (
ID int not null auto_increment, -- anmodningsID er en integer der tæller automatisk op
brugernavn varchar (50) null, -- accepterer strings på længden op til 50
adgangskode varchar (50) null, -- accepterer strings på længden op til 50
brugertype varchar (25) null, -- accepterer datoer som varchar med op til 25 karakterer
primary key (ID) -- den primære nøgle er ID
);

-- Indsætter 5 patienter i tabellen
INSERT INTO Bruger (brugernavn,adgangskode,brugertype)
VALUES
('Hugo','1234','Underviser'),
('Yaasir','1234','Underviser'),
('Bente','1234','Admin');

select* from Bruger