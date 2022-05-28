-- Opretter Kursus tabel
create table if not exists Kurser (
ID int not null auto_increment, -- kursusID er en integer der tæller automatisk op
kursusnavn varchar (50) null, -- accepterer strings på længden op til 50
undervisningstype varchar (50) null, -- accepterer strings på længden op til 50
kursusansvarligID int (5) null, -- accepterer ID'er som integer på op til 5 cifre
primary key (ID), -- den primære nøgle er ID
foreign key (kursusansvarligID) references Bruger(ID) -- foreign key som binder ID'er fra bruger tabellen sammen med kursus tabellen
);

-- Indsætter 3 kurser i tabellen
INSERT INTO Kurser (kursusnavn,undervisningstype,kursusansvarligID)
VALUES
('Systemudvikling','Theo execise',1),
('Systemudvikling','Lecture',1),
('Sygdomslære', 'Forelæsning',2)
;

select* from Kurser