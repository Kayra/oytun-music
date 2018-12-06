SET timezone TO 'Europe/London';

-- INSERT INTO music_site (title, number_of_performances_to_list, number_of_songs_to_list)
-- VALUES ('Oytun',
--         5,
--         5);


INSERT INTO music_performance (venue_name, venue_address, start_time, external_link, 'order')
VALUES ('Troxy',
        '490 Commercial Rd, London E1 0HX',
        (NOW() + interval '1 week'),
        'https://troxy.co.uk/',
        1);
--
-- INSERT INTO music_performance (venue_name, venue_address, start_time, external_link, order)
-- VALUES ('Stoller Hall',
--         'Hunts Bank, Manchester M3 1DA',
--         (NOW() + interval '2 weeks'),
--         'http://stollerhall.com',
--         2);
--
-- INSERT INTO music_performance (venue_name, venue_address, start_time, external_link, order)
-- VALUES ('2 Pigs',
--         'Church St, Cheltenham GL50 3HA',
--         (NOW() + interval '3 week'),
--         'http://2pigs.co.uk',
--         3);
--
--
-- INSERT INTO music_song (title, external_link, order)
-- VALUES ('Song one',
--         'nothing.com',
--         1)
--
-- INSERT INTO music_song (title, external_link, order)
-- VALUES ('Song two',
--         'nothing.com',
--         2)
--
-- INSERT INTO music_song (title, external_link, order)
-- VALUES ('Song three',
--         'nothing.com',
--         3)
