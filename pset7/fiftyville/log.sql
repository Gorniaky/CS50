-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT description
FROM crime_scene_reports
WHERE month = 7 AND day = 28 AND street = "Chamberlin Street";

/*
O roubo do pato CS50 ocorreu às 10h15 no tribunal de Chamberlin Street. As entrevistas foram realizadas hoje com três testemunhas que estavam presentes no momento - cada uma de suas transcrições de entrevista menciona o tribunal.
*/

SELECT name, transcript
FROM interviews
WHERE month = 7 AND day = 28;

/*
Jose | “Ah”, disse ele, “esqueci que não o via há algumas semanas. É uma pequena lembrança do rei da Boêmia em troca de minha ajuda no caso dos papéis de Irene Adler.

Eugene | “Suponho”, disse Holmes, “que quando o Sr. Windibank voltou da França ele ficou muito aborrecido por você ter ido ao baile.”

Barbara | "Você tinha o meu bilhete?" ele perguntou com uma voz profunda e áspera e um forte sotaque alemão. “Eu disse que ligaria.” Ele olhou de um para o outro, como se não tivesse certeza de a quem se dirigir.

Ruth | Em algum momento, dez minutos depois do roubo, vi o ladrão entrar em um carro no estacionamento do tribunal e ir embora. Se você tiver imagens de segurança do estacionamento do tribunal, talvez queira procurar carros que deixaram o estacionamento nesse período.

Eugene | Não sei o nome do ladrão, mas era alguém que reconheci. No início desta manhã, antes de chegar ao tribunal, eu estava passando pelo caixa eletrônico na Fifer Street e vi o ladrão lá sacando algum dinheiro.

Raymond | Quando o ladrão estava saindo do tribunal, eles ligaram para alguém que conversou com eles por menos de um minuto. Na ligação, ouvi o ladrão dizer que eles planejavam pegar o primeiro voo de Fiftyville amanhã. O ladrão então pediu à pessoa do outro lado do telefone para comprar a passagem aérea.
*/

SELECT people.name, people.phone_number, phone_calls.receiver, airports.city
FROM people
JOIN courthouse_security_logs
ON people.license_plate = courthouse_security_logs.license_plate
JOIN atm_transactions
ON people.id = bank_accounts.person_id
JOIN bank_accounts
ON bank_accounts.account_number = atm_transactions.account_number
JOIN phone_calls
ON phone_calls.caller = people.phone_number
JOIN passengers
ON people.passport_number = passengers.passport_number
JOIN flights
ON passengers.flight_id = flights.id
JOIN airports
ON flights.destination_airport_id = airports.id
WHERE courthouse_security_logs.month = 7
AND courthouse_security_logs.day = 28
AND courthouse_security_logs.hour = 10
AND courthouse_security_logs.minute > 15
AND courthouse_security_logs.minute < 25
AND atm_transactions.month = 7
AND atm_transactions.day = 28 
AND atm_transactions.atm_location = "Fifer Street" 
AND atm_transactions.transaction_type = "withdraw"
AND phone_calls.month = 7
AND phone_calls.day = 28
AND phone_calls.duration < 60;

/*
Russell | 26013199 | (770) 555-1861 | (725) 555-3243
Ernest | 49610011 | (367) 555-5533 | (375) 555-8161
Madison | 76054385 | (286) 555-6063 | (676) 555-6554
*/

SELECT DISTINCT(people.name), people.phone_number, phone_calls.caller
FROM people
JOIN phone_calls
ON phone_calls.receiver = people.phone_number
WHERE people.phone_number IN (
SELECT phone_calls.receiver
FROM people
JOIN courthouse_security_logs
ON people.license_plate = courthouse_security_logs.license_plate
JOIN atm_transactions
ON people.id = bank_accounts.person_id
JOIN bank_accounts
ON bank_accounts.account_number = atm_transactions.account_number
JOIN phone_calls
ON phone_calls.caller = people.phone_number
JOIN passengers
ON people.passport_number = passengers.passport_number
JOIN flights
ON passengers.flight_id = flights.id
JOIN airports
ON flights.origin_airport_id = airports.id
WHERE courthouse_security_logs.month = 7
AND courthouse_security_logs.day = 28
AND courthouse_security_logs.hour = 10
AND courthouse_security_logs.minute > 15
AND courthouse_security_logs.minute < 25
AND atm_transactions.month = 7
AND atm_transactions.day = 28 
AND atm_transactions.atm_location = "Fifer Street" 
AND atm_transactions.transaction_type = "withdraw"
AND phone_calls.month = 7
AND phone_calls.day = 28
AND phone_calls.duration < 60
AND airports.city = "Fiftyville"
);