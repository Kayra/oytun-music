SET timezone TO 'Europe/London';

INSERT INTO music_site (title, number_of_performances_to_display, number_of_songs_to_display) VALUES
  ('Oytun', 5, 5);


INSERT INTO music_performance (venue_name, venue_address, start_time, external_link, display_order) VALUES
  ('Troxy', '490 Commercial Rd, London E1 0HX', (NOW() + interval '1 week'), 'https://troxy.co.uk/', 1),
  ('Stoller Hall', 'Hunts Bank, Manchester M3 1DA', (NOW() + interval '2 weeks'), 'http://stollerhall.com', 2),
  ('2 Pigs', 'Church St, Cheltenham GL50 3HA', (NOW() + interval '3 week'), 'http://2pigs.co.uk', 3);

INSERT INTO music_song (title, external_link, display_order) VALUES
  ('Condor Ave', 'uploads/Condor_Ave.mp3', 1),
  ('A Good Man Is Hard To Find', 'uploads/A_Good_Man_Is_Hard_To_Find.mp3', 2),
  ('Happy Birthday', 'uploads/Happy_Birthday.mp3', 3);
