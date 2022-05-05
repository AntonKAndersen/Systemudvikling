-- Opretter bruger tabel
create table if not exists Lokaler (
ID int not null auto_increment, -- anmodningsID er en integer der tæller automatisk op
lokale varchar (50) null, -- accepterer strings på længden op til 50
placering varchar (50) null, -- accepterer strings på længden op til 50
universitet varchar (50) null, -- accepterer datoer som varchar med op til 25 karakterer
primary key (ID) -- den primære nøgle er ID
);

-- Indsætter 5 patienter i tabellen
INSERT INTO Lokaler (lokale,placering,universitet)
VALUES
('Und.lokale - A105','HCØ','Københavns Universitet'),
('Und.lokale - A112','HCØ','Københavns Universitet'),
('Aud. - Lille UP1', 'DIKU', 'Københavns Universitet'),
('Aud. - Niels K. Jerne', 'Panum', 'Københavns Universitet'),
('bi - 2-1-17', 'Biocenter', 'Københavns Universitet'),
('X2.70', 'DTU Ballerup Campus', 'Danmarks Tekniske Universitet')
;

select* from Lokaler