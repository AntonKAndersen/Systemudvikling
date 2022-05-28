-- Opretter bruger tabel
create table if not exists Bruger (
ID int not null auto_increment, -- brugerID er en integer der tæller automatisk op
brugernavn varchar (50) null, -- accepterer strings på længden op til 50
adgangskode varchar (50) null, -- accepterer strings på længden op til 50
brugertype varchar (25) null, -- accepterer strings op til 25 karakterer
fuldtnavn  varchar (50) null, -- accepterer strings på længden op til 50
primary key (ID) -- den primære nøgle er ID
);

-- Indsætter 3 brugere i tabellen
INSERT INTO Bruger (brugernavn,adgangskode,brugertype,fuldtnavn)
VALUES
('Hugo','1234','Underviser', 'Hugo Andrés López'),
('Yaasir','1234','Underviser', 'Yaasir A. M. Gabeyre'),
('Bente','1234','Admin', 'Bente Bent');

select* from Bruger