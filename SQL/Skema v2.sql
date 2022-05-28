-- Opretter anmodnings tabel
create table if not exists Skema (
ID int not null auto_increment, -- lektionsID er en integer der tæller automatisk op
kursusansvarligID int (5) null, -- accepterer kursusansvarligID'er på op til 5 cifre
kursusID int (5) null, -- accepterer kursusID'er på op til 5 cifre
lokaleID int (5) null, -- accepterer lokaleID'er på op til 5 cifre
dato char (10) null, -- accepterer datoer som string med en FIXED længde på 10 karakterer / kunne også have brugt datatype DATE
tid char (11) null, -- accepterer tidsrum som char kun med længden 11 karakterer / kunne også have brugt datatype TIME
primary key (ID), -- den primære nøgle er ID
foreign key (lokaleID) references Lokaler(ID), -- foreign key som binder ID'er fra lokale tabellen sammen med skema tabellen 
foreign key (kursusansvarligID) references Bruger(ID), -- foreign key som binder ID'er fra bruger tabellen sammen med skema tabellen 
foreign key (kursusID) references Kurser(ID) -- foreign key som binder ID'er fra kursus tabellen sammen med skema tabellen 
);

-- Indsætter 3 lektioner i tabellen
INSERT INTO Skema (kursusansvarligID,kursusID,lokaleID,dato,tid)
VALUES
(1,1,1,'24-04-2022','09:00-12:00'),
(1,2,2,'27-04-2022','15:00-17:00'),
(2,3,4,'30-04-2022','09:00-12:00');

select * from Skema