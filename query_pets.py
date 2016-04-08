#!user/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys




def dataLookup():
    userInput = None

    try:

        while userInput != -1:
            userInput = raw_input('Please input a person\'s ID number: ')
            userInput2 = userInput
            con = lite.connect('pets.db')
            cur = con.cursor()
            cur2 = con.cursor()
            cur.execute('SELECT first_name, last_name FROM'
                        ' person WHERE id = ?', (userInput))

            cur2.execute('SELECT pet.name, pet.breed, pet.age, pet.dead '
                         'FROM pet '
                         'INNER JOIN person_pet '
                         'ON pet.id = person_pet.pet_id '
                         'INNER JOIN person '
                         'ON person_pet.person_id = person.id '
                         'WHERE person.id = ?', (userInput2))

            rows = cur.fetchall()
            rows2 = cur2.fetchall()


            print '\nName: {} {}'.format(rows[0][0], rows[0][1])
            print 'Pet Name: {} \nPet Breed: {} \nPet Age: {} \nPet' \
                  'Alive or Dead: {}\n'.format(rows2[0][0], rows2[0][1],
                                              rows2[0][2], rows2[0][3])



            con.commit()

    except lite.Error, e:

        if con:
            con.rollback()

            print "Error {}".format(e)
            dataLookup()
        else:
            sys.exit()


if __name__ == '__main__':
    dataLookup()
