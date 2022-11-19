import unittest
import statistics
import math
import numpy as np


class MeanTest(unittest.TestCase):
    def test_small(self):
        l = [5,3,9]
        res = mean(l)
        expected = statistics.mean(l)
        self.assertAlmostEqual(res, expected)

    def test_same(self):
        l = [5,5]
        res = mean(l)
        expected = statistics.mean(l)
        self.assertAlmostEqual(res, expected)

    def test_large(self):
        l = [5,6,365,3,8,0,4,56]
        res = mean(l)
        expected = statistics.mean(l)
        self.assertAlmostEqual(res, expected)

    def test_negative(self):
        l = [-4,0,8]
        res = mean(l)
        expected = statistics.mean(l)
        self.assertAlmostEqual(res, expected)


class VarTest(unittest.TestCase):
    def test_small(self):
        l = [5,3,9]
        res = variance(l)
        expected = statistics.variance(l)
        self.assertAlmostEqual(res, expected)

    def test_same(self):
        l = [5,5]
        res = variance(l)
        expected = statistics.variance(l)
        self.assertAlmostEqual(res, expected)

    def test_large(self):
        l = [5,6,365,3,8,0,4,56]
        res = variance(l)
        expected = statistics.variance(l)
        self.assertAlmostEqual(res, expected)

    def test_negative(self):
        l = [-4,0,8]
        res = variance(l)
        expected = statistics.variance(l)
        self.assertAlmostEqual(res, expected)


class MedianTest(unittest.TestCase):
    def test_even(self):
        res = median([9,3,6,5])
        expected = 5.5
        self.assertEqual(res, expected)

    def test_odd(self):
        res = median([1,3,4])
        expected = 3
        self.assertEqual(res, expected)

    def test_single(self):
        res = median([4])
        expected = 4
        self.assertEqual(res, expected)


class SumDigitsTest(unittest.TestCase):
    def test_long(self):
        res = sum_digits(1339439345)
        expected = 44
        self.assertEqual(res, expected)

    def test_small(self):
        res = sum_digits(9)
        expected = 9
        self.assertEqual(res, expected)

    def test_zero(self):
        res = sum_digits(0)
        expected = 0
        self.assertEqual(res, expected)

    def test_one(self):
        res = sum_digits(1)
        expected = 1
        self.assertEqual(res, expected)


class LevenshteinDistanceTest(unittest.TestCase):
    def test_small(self):
        a = "ab"
        b = "ba"
        res = lev(a, b)
        expected = 2
        self.assertEqual(res, expected)

    def test_normal(self):
        a = "book"
        b = "back"
        res = lev(a, b)
        expected = 2
        self.assertEqual(res, expected)

    def test_equal(self):
        a = "house"
        b = "house"
        res = lev(a, b)
        expected = 0
        self.assertEqual(res, expected)

    def test_long(self):
        a = "abcdefghi"
        b = "rstuvwxyz"
        res = lev(a, b)
        expected = 9
        self.assertEqual(res, expected)


class MovieTest(unittest.TestCase):
    def test_movie_ctor(self):
        m = Movie("Avatar", 2009, "ACTION")
        expected_title = "Avatar"
        expected_year = 2009
        expected_genre = "ACTION"
        self.assertEqual(m.title, expected_title)
        self.assertEqual(m.year, expected_year)
        self.assertEqual(m.genre, expected_genre)

    def test_movie_get_title(self):
        m = Movie("Avatar", 2009, "ACTION")
        expected_title = "Avatar"
        self.assertEqual(m.get_title(), expected_title)

    def test_movie_get_year(self):
        m = Movie("Avatar", 2009, "ACTION")
        expected_year = 2009
        self.assertEqual(m.get_year(), expected_year)

    def test_movie_get_genre(self):
        m = Movie("Avatar", 2009, "ACTION")
        expected_genre = "ACTION"
        self.assertEqual(m.get_genre(), expected_genre)

    def test_movie_eq(self):
        m = Movie("Avatar", 2009, "ACTION")
        m_eq = Movie("Avatar", 2009, "ACTION")
        m_neq = Movie("Avata", 2009, "ACTION")
        m_neq2 = Movie("Avatar", 2090, "ACTION")
        m_neq3 = Movie("Avatar", 2009, "HORROR")
        self.assertEqual(m, m_eq)
        self.assertNotEqual(m, m_neq)
        self.assertNotEqual(m, m_neq2)
        self.assertNotEqual(m, m_neq3)


class PersonTest(unittest.TestCase):
    def test_person_ctor(self):
        p = Person("Erika", "Mustermann")
        expected_name = "Erika"
        expected_surname = "Mustermann"
        self.assertEqual(p.name, expected_name)
        self.assertEqual(p.surname, expected_surname)

    def test_person_get_name(self):
        p = Person("Erika", "Mustermann")
        expected_name = "Erika"
        self.assertEqual(p.get_name(), expected_name)

    def test_person_get_surname(self):
        p = Person("Erika", "Mustermann")
        expected_surname = "Mustermann"
        self.assertEqual(p.get_surname(), expected_surname)

    def test_director_ctor(self):
        m = Movie("Avatar", 2009, "ACTION")
        d = Director("Erika", "Mustermann", m)
        expected_name = "Erika"
        expected_surname = "Mustermann"
        expected_movie = Movie("Avatar", 2009, "ACTION")
        self.assertEqual(d.name, expected_name)
        self.assertEqual(d.surname, expected_surname)
        self.assertEqual(d.movie, expected_movie)

    def test_director_inheritance(self):
        self.assertTrue(issubclass(Director, Person))

    def test_director_get_movie(self):
        m = Movie("Avatar", 2009, "ACTION")
        d = Director("Erika", "Mustermann", m)
        expected_movie = Movie("Avatar", 2009, "ACTION")
        self.assertEqual(d.get_movie(), expected_movie)

    def test_director_actor_in_movie(self):
        m_avatar = Movie("Avatar", 2009, "ACTION")
        m_titans = Movie("Clash of the Titans", 2010, "ACTION")
        d_cameron = Director("James", "Cameron", m_avatar)
        d_leterrier = Director("Louis", "Leterrier", m_titans)
        a_worthington = Actor("Sam", "Worthington", [m_avatar, m_titans])
        self.assertTrue(d_cameron.actor_in_movie(a_worthington))

    def test_director_actor_not_in_movie(self):
        m_avatar = Movie("Avatar", 2009, "ACTION")
        m_titans = Movie("Clash of the Titans", 2010, "ACTION")
        d_cameron = Director("James", "Cameron", m_avatar)
        d_leterrier = Director("Louis", "Leterrier", m_titans)
        a_neeson= Actor("Liam", "Neeson", [m_titans])
        self.assertFalse(d_cameron.actor_in_movie(a_neeson))

    def test_actor_ctor(self):
        m_avatar = Movie("Avatar", 2009, "ACTION")
        m_titans = Movie("Clash of the Titans", 2010, "ACTION")
        a = Actor("Olivia", "Wilde", [m_avatar, m_titans])
        movies = [m_avatar, m_titans]
        self.assertEqual(a.movies, movies)

    def test_actor_get_all_movies(self):
        m_avatar = Movie("Avatar", 2009, "ACTION")
        m_titans = Movie("Clash of the Titans", 2010, "ACTION")
        a = Actor("Olivia", "Wilde", [m_avatar, m_titans])
        movies = [m_avatar, m_titans]
        self.assertEqual(a.get_all_movies(), movies)

    def test_actor_get_movies_contrained(self):
        m_avatar = Movie("Avatar", 2009, "ACTION")
        m_titans = Movie("Clash of the Titans", 2010, "ACTION")
        m_it     = Movie("It", 2017, "HORROR")
        a = Actor("Olivia", "Wilde", [m_avatar, m_titans])
        movies = [m_titans]
        self.assertEqual(a.get_movies("ACTION", 2009), movies)

    def test_actor_inheritance(self):
        self.assertTrue(issubclass(Actor, Person))

class HammingDistanceTest(unittest.TestCase):
    def test_small(self):
        a = "ab"
        b = "ba"
        res = hamming_distance_custom(a, b)
        expected = 2
        self.assertEqual(res, expected)

    def test_normal(self):
        a = "book"
        b = "back"
        res = hamming_distance_custom(a, b)
        expected = 2
        self.assertEqual(res, expected)

    def test_equal(self):
        a = "house"
        b = "house"
        res = hamming_distance_custom(a, b)
        expected = 0
        self.assertEqual(res, expected)

    def test_long(self):
        a = "abcdefghi"
        b = "rstuvwxyz"
        res = hamming_distance_custom(a, b)
        expected = 9
        self.assertEqual(res, expected)

    def test_different_length(self):
        a = "ab"
        b = "abc"
        res = hamming_distance_custom(a, b)
        expected = math.inf
        self.assertEqual(res, expected)

    def test_empty(self):
        a = ""
        b = ""
        res = hamming_distance_custom(a, b)
        expected = 0
        self.assertEqual(res, expected)


class DuplicatesTest(unittest.TestCase):
    def test_duplicates(self):
        expected_duplicates = ['Harry Potter and the Deathly Hallows: Part 2', 'The Graet Wall', 'Frozem', 'The Lego Movoe']
        self.assertCountEqual(duplicate_movies, expected_duplicates)


class MissingTest(unittest.TestCase):
    def test_missing_values(self):
        d = {'Title': ["Allied", "Django Unchained", "Les Misérables", "Man of Steel"],
             'Genre': [np.nan, "Drama,Western", "Drama,Musical,Romance", "Action,Adventure,Fantasy"],
             'Director': ["Robert Zemeckis", np.nan, "Tom Hooper", "Zack Snyder"],
             'Actors': ['Brad Pitt, Marion Cotillard, Jared Harris, Vincent Ebrahim','Jamie Foxx, Christoph Waltz, Leonardo DiCaprio,Kerry Washington', 'Hugh Jackman, Russell Crowe, Anne Hathaway,Amanda Seyfried', 'Henry Cavill, Amy Adams, Michael Shannon, Diane Lane'],
             'Year': [2016.0, 2012.0, 2012.0, np.nan],
             'Rating': [7.1, 8.4, np.nan, 7.1]
            }
        expected_df = pd.DataFrame(data=d, index=[71, 145, 246, 295])
        self.assertTrue(df_missing.equals(expected_df))


class OutliersTest(unittest.TestCase):
    def test_outliers(self):
        d = {'Title': ["Snowpiercer", "P.S. I Love You", "The Rise of the Krays"],
             'Genre': ["Action,Drama,Sci-Fi", "Drama,Romance", "Crime,Drama"],
             'Director': ["Bong Joon Ho", "Richard LaGravenese", "Zackary Adler"],
             'Actors': ["Chris Evans, Jamie Bell, Tilda Swinton, Ed Harris", "Hilary Swank, Gerard Butler, Harry Connick Jr., Lisa Kudrow", "Matt Vael, Simon Cotton, Kevin Leslie, Olivia Moyles"],
             'Year': [2013.0, 1995.0, 2015.0],
             'Rating': [-2, 7.1, 12.1]}
        expected_df = pd.DataFrame(data=d, index=[316, 545, 606])
        self.assertTrue(df_outliers.equals(expected_df))
