-- Opretter anmodnings tabel
create table if not exists Anmodninger (
ID int not null auto_increment, -- anmodningsID er en integer der tæller automatisk op
kursusansvarligID int (5) null, -- accepterer strings på længden op til 50
kursusID int (5) null, -- accepterer strings på længden op til 50
dato char (10) null, -- accepterer datoer som string med en FIXED længde på 10 karakterer / kunne også have brugt datatype DATE
tid char (11) null, -- accepterer tidsrum som char kun med længden 11 karakterer / kunne også have brugt datatype TIME
primary key (ID), -- den primære nøgle er ID
foreign key (kursusansvarligID) references Bruger(ID), -- foreign key som binder ID'er fra bruger tabellen sammen med anmodnings tabellen 
foreign key (kursusID) references Kurser(ID) -- foreign key som binder ID'er fra kursus tabellen sammen med anmodnings tabellen 
);

-- Indsætter 3 anmodninger i tabellen
INSERT INTO Anmodninger (kursusansvarligID,kursusID,dato,tid)
VALUES
(1,1,'24-04-2022','09:00-12:00'),
(1,2,'26-04-2022','15:00-17:00'),
(2,3,'27-04-2022','09:00-12:00');

select* from Anmodninger
