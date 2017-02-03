# -*- coding: iso-8859-15 -*-
from pprint import pprint

from bson import ObjectId

from app.database.facebook_objects import FbPost

post = FbPost()
post.id = ObjectId("5893bbd54520006bc3fad5c1")
post.created_time = 9991235556703


def convert2unicode(mydict):
    for k, v in mydict.iteritems():
        if isinstance(v, str):
            mydict[k] = unicode(v, errors='replace')
        elif isinstance(v, dict):
            convert2unicode(v)
    return mydict


x = {
    "id": "10154127934361867",
    "from": {
        "name": "Open Vld",
        "id": "53668151866"
    },
    "link": "https://www.facebook.com/openvld/photos/a.61804781866.84643.53668151866/10154127934361867/?type=3",
    "picture": "https://scontent.xx.fbcdn.net/v/t1.0-0/s130x130/15741197_10154127934361867_180498785327474225_n.jpg?oh=3b42a93c6e2e3ecf3067ab55df3fa754&oe=59471122",
    "comments": {
        "data": [
            {
                "likes": {
                    "data": [
                        {
                            "link": "https://www.facebook.com/openvld/",
                            "id": "53668151866",
                            "name": "Open Vld",
                            "profile_type": "page",
                            "username": "openvld"
                        },
                        {
                            "link": "https://www.facebook.com/app_scoped_user_id/10206953167940745/",
                            "id": "10206953167940745",
                            "name": "Anne Frérart",
                            "profile_type": "user"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "NTM2NjgxNTE4NjYZD",
                            "after": "MTAyMDY5NTMxNjc5NDA3NDUZD"
                        }
                    }
                },
                "comment_count": 5,
                "id": "10154127934361867_10154128013606867"
            },
            {
                "likes": {
                    "data": [
                        {
                            "link": "https://www.facebook.com/openvld/",
                            "id": "53668151866",
                            "name": "Open Vld",
                            "profile_type": "page",
                            "username": "openvld"
                        },
                        {
                            "link": "https://www.facebook.com/app_scoped_user_id/10206953167940745/",
                            "id": "10206953167940745",
                            "name": "Anne Frérart",
                            "profile_type": "user"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "NTM2NjgxNTE4NjYZD",
                            "after": "MTAyMDY5NTMxNjc5NDA3NDUZD"
                        }
                    }
                },
                "comment_count": 0,
                "id": "10154127934361867_10154128044681867"
            },
            {
                "likes": {
                    "data": [
                        {
                            "link": "https://www.facebook.com/openvld/",
                            "id": "53668151866",
                            "name": "Open Vld",
                            "profile_type": "page",
                            "username": "openvld"
                        },
                        {
                            "link": "https://www.facebook.com/app_scoped_user_id/10206953167940745/",
                            "id": "10206953167940745",
                            "name": "Anne Frérart",
                            "profile_type": "user"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "NTM2NjgxNTE4NjYZD",
                            "after": "MTAyMDY5NTMxNjc5NDA3NDUZD"
                        }
                    }
                },
                "comment_count": 0,
                "id": "10154127934361867_10154127939196867"
            },
            {
                "likes": {
                    "data": [
                        {
                            "link": "https://www.facebook.com/openvld/",
                            "id": "53668151866",
                            "name": "Open Vld",
                            "profile_type": "page",
                            "username": "openvld"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "NTM2NjgxNTE4NjYZD",
                            "after": "NTM2NjgxNTE4NjYZD"
                        }
                    }
                },
                "comment_count": 0,
                "id": "10154127934361867_10154128883511867"
            },
            {
                "likes": {
                    "data": [
                        {
                            "link": "https://www.facebook.com/openvld/",
                            "id": "53668151866",
                            "name": "Open Vld",
                            "profile_type": "page",
                            "username": "openvld"
                        },
                        {
                            "link": "https://www.facebook.com/app_scoped_user_id/10206953167940745/",
                            "id": "10206953167940745",
                            "name": "Anne Frérart",
                            "profile_type": "user"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "NTM2NjgxNTE4NjYZD",
                            "after": "MTAyMDY5NTMxNjc5NDA3NDUZD"
                        }
                    }
                },
                "comment_count": 0,
                "id": "10154127934361867_10154128305841867"
            },
            {
                "comment_count": 0,
                "id": "10154127934361867_10154130859186867"
            },
            {
                "likes": {
                    "data": [
                        {
                            "link": "https://www.facebook.com/openvld/",
                            "id": "53668151866",
                            "name": "Open Vld",
                            "profile_type": "page",
                            "username": "openvld"
                        },
                        {
                            "link": "https://www.facebook.com/app_scoped_user_id/10206953167940745/",
                            "id": "10206953167940745",
                            "name": "Anne Frérart",
                            "profile_type": "user"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "NTM2NjgxNTE4NjYZD",
                            "after": "MTAyMDY5NTMxNjc5NDA3NDUZD"
                        }
                    }
                },
                "comment_count": 0,
                "id": "10154127934361867_10154128764521867"
            },
            {
                "likes": {
                    "data": [
                        {
                            "link": "https://www.facebook.com/app_scoped_user_id/977594442266324/",
                            "id": "977594442266324",
                            "name": "Jeroen Jacobs",
                            "profile_type": "user"
                        },
                        {
                            "link": "https://www.facebook.com/app_scoped_user_id/1012027898825368/",
                            "id": "1012027898825368",
                            "name": "Marc Van Melder",
                            "profile_type": "user"
                        },
                        {
                            "link": "https://www.facebook.com/app_scoped_user_id/10153269983585286/",
                            "id": "10153269983585286",
                            "name": "Reina De Niel-Keenan",
                            "profile_type": "user"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "OTc3NTk0NDQyMjY2MzI0",
                            "after": "MTAxNTMyNjk5ODM1ODUyODYZD"
                        }
                    }
                },
                "comment_count": 0,
                "id": "10154127934361867_10154130575471867"
            },
            {
                "comment_count": 0,
                "id": "10154127934361867_10154131814186867"
            },
            {
                "comment_count": 0,
                "id": "10154127934361867_10154129351641867"
            },
            {
                "comment_count": 0,
                "id": "10154127934361867_10154129322496867"
            }
        ],
        "paging": {
            "cursors": {
                "before": "MTEZD",
                "after": "MQZDZD"
            }
        }
    },
    "reactions": {
        "data": [
            {
                "id": "807866175999596",
                "name": "Walter Boschmans",
                "type": "LIKE"
            },
            {
                "id": "1125963157429495",
                "name": "Marie Louise Podevijn",
                "type": "LIKE"
            },
            {
                "id": "251397401966685",
                "name": "Rita Leunis",
                "type": "LIKE"
            },
            {
                "id": "10211093600885663",
                "name": "Marcel Devogeleer",
                "type": "LOVE"
            },
            {
                "id": "112834222386687",
                "name": "Penne Placide",
                "type": "LIKE"
            },
            {
                "id": "982866211769641",
                "name": "Anja Deridder",
                "type": "LIKE"
            },
            {
                "id": "544944078942734",
                "name": "Jef Haesaerts",
                "type": "HAHA"
            },
            {
                "id": "10203543710784322",
                "name": "Kevin Ricciolini",
                "type": "LIKE"
            },
            {
                "id": "10209788850145074",
                "name": "Chris Verhaeghe",
                "type": "LIKE"
            },
            {
                "id": "10205766781956060",
                "name": "Hubert Portaels",
                "type": "LIKE"
            },
            {
                "id": "321773728181497",
                "name": "Dina D'haene",
                "type": "LIKE"
            },
            {
                "id": "600896990065730",
                "name": "Lutgarde Hulsmans",
                "type": "LIKE"
            },
            {
                "id": "10203803368354214",
                "name": "De Neef Regina",
                "type": "LOVE"
            },
            {
                "id": "1534424340145773",
                "name": "Thierry Voet",
                "type": "LIKE"
            },
            {
                "id": "396827240668294",
                "name": "Arlette Van Der Meersch",
                "type": "LIKE"
            },
            {
                "id": "10207999502372158",
                "name": "Julie Van Hoorick",
                "type": "LIKE"
            },
            {
                "id": "550622208403560",
                "name": "Josee Entbrouxk",
                "type": "LIKE"
            },
            {
                "id": "201277740218632",
                "name": "Luc Leterme",
                "type": "LIKE"
            },
            {
                "id": "1467217000265106",
                "name": "Carine Devos",
                "type": "LIKE"
            },
            {
                "id": "1880083942218117",
                "name": "Jeanine Matthys",
                "type": "LIKE"
            },
            {
                "id": "10205621626806205",
                "name": "Philippe Heyvaert",
                "type": "LIKE"
            },
            {
                "id": "1470440159879431",
                "name": "Christel Ceulemans",
                "type": "LIKE"
            },
            {
                "id": "955442697814748",
                "name": "Sonja Regelbrugge",
                "type": "LIKE"
            },
            {
                "id": "1048603871906795",
                "name": "Godelieve Bauters",
                "type": "LIKE"
            },
            {
                "id": "798344736870980",
                "name": "Carina Boffin",
                "type": "LIKE"
            }
        ],
        "paging": {
            "cursors": {
                "before": "TVRBd01EQXpNamcyTmpJM01EYzRPakUwT0RNME5qWTROVEE2TWpVME1EazJNVFl4TXc9PQZDZD",
                "after": "TVRBd01EQXdPRFl6T0RNMU5qRXlPakUwT0RNek5qY3hPVEk2TWpVME1EazJNVFl4TXc9PQZDZD"
            },
            "next": "https://graph.facebook.com/v2.8/10154127934361867/reactions?access_token=EAACEdEose0cBAP5JV6T9tgfMye4FWqBlZCZBbDvknoNZA1gxb2ujnXGOrZAQZAANsfYZCyPJhFyHZABGZCoQOX7I5P90MZAZBRVCg7LL4ID6gAYbHZAxZB7fdgXZAZCejTvxfGv4L5XGP5bIaH4GX1CcZBAuHPyPzHuHQ0UGV4ilV3iBXTumdALFNE0aoLHCEoi64aTd14ZD&pretty=0&limit=25&after=TVRBd01EQXdPRFl6T0RNMU5qRXlPakUwT0RNek5qY3hPVEk2TWpVME1EazJNVFl4TXc9PQZDZD"
        }
    },
    "sharedposts": {
        "data": [
            {
                "from": {
                    "name": "UwMeningTelt",
                    "id": "237342893035603"
                },
                "created_time": "2017-01-03T17:00:12+0000",
                "description": "Beste wensen voor 2017! Open Vld wenst je een jaar vol vrijheid.",
                "id": "237342893035603_830337680402785",
                "message": "Beste wensen voor 2017, vanwege Open Vld Boutersem! Ook in 2017 blijven wij ijveren voor een positiever Boutersem!",
                "story": "UwMeningTelt shared Open Vld's photo.",
                "type": "photo"
            },
            {
                "from": {
                    "name": "Open Vld Boutersem",
                    "id": "151910354939694"
                },
                "created_time": "2017-01-03T16:58:07+0000",
                "description": "Beste wensen voor 2017! Open Vld wenst je een jaar vol vrijheid.",
                "id": "151910354939694_947850935345628",
                "message": "Beste wensen voor 2017, vanwege Open Vld Boutersem! Ook in 2017 blijven wij ijveren voor een positiever Boutersem!",
                "story": "Open Vld Boutersem shared Open Vld's photo.",
                "type": "photo",
                "reactions": {
                    "data": [
                        {
                            "id": "1056235081057016",
                            "name": "Dany Peerenbooms",
                            "type": "LIKE"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "TVRBd01EQXdNVEUyTURJM05EYzJPakUwT0RNME5qUXpOemc2TWpVME1EazJNVFl4TXc9PQZDZD",
                            "after": "TVRBd01EQXdNVEUyTURJM05EYzJPakUwT0RNME5qUXpOemc2TWpVME1EazJNVFl4TXc9PQZDZD"
                        }
                    }
                },
                "likes": {
                    "data": [
                        {
                            "id": "1056235081057016",
                            "name": "Dany Peerenbooms"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "MTA1NjIzNTA4MTA1NzAxNgZDZD",
                            "after": "MTA1NjIzNTA4MTA1NzAxNgZDZD"
                        }
                    }
                }
            },
            {
                "from": {
                    "name": "Open VLD Nieuwpoort",
                    "id": "274469919262324"
                },
                "created_time": "2017-01-02T15:09:51+0000",
                "description": "Beste wensen voor 2017! Open Vld wenst je een jaar vol vrijheid.",
                "id": "274469919262324_1393077977401507",
                "story": "Open VLD Nieuwpoort shared Open Vld's photo.",
                "type": "photo",
                "reactions": {
                    "data": [
                        {
                            "id": "759191354164458",
                            "name": "Stefaan Desaever",
                            "type": "LIKE"
                        },
                        {
                            "id": "855138874511598",
                            "name": "Brigitte Deroose",
                            "type": "LIKE"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "TVRBd01EQXlNakE0TURJME1UQXdPakUwT0RNek9UTTVOVGc2TWpVME1EazJNVFl4TXc9PQZDZD",
                            "after": "TVRBd01EQXdORFkwT0RBMk1UQTNPakUwT0RNek56SXhPRE02TWpVME1EazJNVFl4TXc9PQZDZD"
                        }
                    }
                },
                "likes": {
                    "data": [
                        {
                            "id": "759191354164458",
                            "name": "Stefaan Desaever"
                        },
                        {
                            "id": "855138874511598",
                            "name": "Brigitte Deroose"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "NzU5MTkxMzU0MTY0NDU4",
                            "after": "ODU1MTM4ODc0NTExNTk4"
                        }
                    }
                }
            },
            {
                "from": {
                    "name": "Open VLD 1210sjtn",
                    "id": "857655011068802"
                },
                "created_time": "2017-01-02T08:37:51+0000",
                "description": "Beste wensen voor 2017! Open Vld wenst je een jaar vol vrijheid.",
                "id": "857655011068802_906084499559186",
                "message": "Beste wensen voor 2017! Open Vld wenst je een jaar vol vrijheid!",
                "story": "Open VLD 1210sjtn shared Open Vld's photo.",
                "type": "photo",
                "reactions": {
                    "data": [
                        {
                            "id": "10152945410941695",
                            "name": "Senna Et-tahiri",
                            "type": "LIKE"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "TmpZAMk16VTJOamswT2pFME9ETXpOVFV5T0RVNk1qVTBNRGsyTVRZAeE13PT0ZD",
                            "after": "TmpZAMk16VTJOamswT2pFME9ETXpOVFV5T0RVNk1qVTBNRGsyTVRZAeE13PT0ZD"
                        }
                    }
                },
                "likes": {
                    "data": [
                        {
                            "id": "10152945410941695",
                            "name": "Senna Et-tahiri"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "MTAxNTI5NDU0MTA5NDE2OTUZD",
                            "after": "MTAxNTI5NDU0MTA5NDE2OTUZD"
                        }
                    }
                }
            },
            {
                "from": {
                    "name": "Open Vld Brussel",
                    "id": "1589760981258549"
                },
                "created_time": "2017-01-01T18:52:46+0000",
                "description": "Beste wensen voor 2017! Open Vld wenst je een jaar vol vrijheid.",
                "id": "1589760981258549_1882947668606544",
                "story": "Open Vld Brussel shared Open Vld's photo.",
                "type": "photo",
                "reactions": {
                    "data": [
                        {
                            "id": "10205181727195692",
                            "name": "Hielkje de Roos",
                            "type": "LIKE"
                        },
                        {
                            "id": "1814763795462353",
                            "name": "Willy Nuel",
                            "type": "LIKE"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "TVRBeU1EY3lOVEV6TnpveE5EZA3pNelEzTXpRek9qSTFOREE1TmpFMk1UTT0ZD",
                            "after": "TVRBd01EQTNPRFl5TkRrM01USXpPakUwT0RNek1ERTROams2TWpVME1EazJNVFl4TXc9PQZDZD"
                        }
                    }
                },
                "likes": {
                    "data": [
                        {
                            "id": "10205181727195692",
                            "name": "Hielkje de Roos"
                        },
                        {
                            "id": "1814763795462353",
                            "name": "Willy Nuel"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "MTAyMDUxODE3MjcxOTU2OTIZD",
                            "after": "MTgxNDc2Mzc5NTQ2MjM1MwZDZD"
                        }
                    }
                }
            },
            {
                "from": {
                    "name": "Open VLD Niel",
                    "id": "996900070326561"
                },
                "created_time": "2017-01-01T16:08:19+0000",
                "description": "Beste wensen voor 2017! Open Vld wenst je een jaar vol vrijheid.",
                "id": "996900070326561_1580685708614658",
                "message": "Beste wensen voor 2017! Open Vld Niel wenst u een jaar vol vrijheid!",
                "story": "Open VLD Niel shared Open Vld's photo.",
                "type": "photo",
                "reactions": {
                    "data": [
                        {
                            "id": "10204559382857125",
                            "name": "Vera van Dijck",
                            "type": "LIKE"
                        },
                        {
                            "id": "1099075243444778",
                            "name": "Gie Wyckmans",
                            "type": "LIKE"
                        },
                        {
                            "id": "210485299422002",
                            "name": "Michel Stevens",
                            "type": "LIKE"
                        },
                        {
                            "id": "1240171756090216",
                            "name": "Anita Verschueren",
                            "type": "LIKE"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "TVRZAeE1ETXlNRGMzTWpveE5EZA3pPVGMyT1RVM09qSTFOREE1TmpFMk1UTT0ZD",
                            "after": "TVRBd01EQXlPVEl5TURrME1qRTRPakUwT0RNeU9EY3dNekU2TWpVME1EazJNVFl4TXc9PQZDZD"
                        }
                    }
                },
                "likes": {
                    "data": [
                        {
                            "id": "10204559382857125",
                            "name": "Vera van Dijck"
                        },
                        {
                            "id": "1099075243444778",
                            "name": "Gie Wyckmans"
                        },
                        {
                            "id": "210485299422002",
                            "name": "Michel Stevens"
                        },
                        {
                            "id": "1240171756090216",
                            "name": "Anita Verschueren"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "MTAyMDQ1NTkzODI4NTcxMjUZD",
                            "after": "MTI0MDE3MTc1NjA5MDIxNgZDZD"
                        }
                    }
                }
            },
            {
                "from": {
                    "name": "Open VLD Haacht",
                    "id": "131618487010457"
                },
                "created_time": "2017-01-01T13:55:09+0000",
                "description": "Beste wensen voor 2017! Open Vld wenst je een jaar vol vrijheid.",
                "id": "131618487010457_631984230307211",
                "message": "Open VLD Haacht wenst u een fijn 2017 !!",
                "story": "Open VLD Haacht shared Open Vld's photo.",
                "type": "photo",
                "reactions": {
                    "data": [
                        {
                            "id": "10205642438252116",
                            "name": "Rombauts Liliane",
                            "type": "LIKE"
                        },
                        {
                            "id": "10200799741795383",
                            "name": "Kristel Andries",
                            "type": "LIKE"
                        },
                        {
                            "id": "777088352349300",
                            "name": "Karin Derua",
                            "type": "LIKE"
                        },
                        {
                            "id": "10203468894942478",
                            "name": "Ilse Fillet",
                            "type": "LIKE"
                        },
                        {
                            "id": "623417957794168",
                            "name": "Mariette Van Noten",
                            "type": "LIKE"
                        },
                        {
                            "id": "131618487010457",
                            "name": "Open VLD Haacht",
                            "type": "LIKE"
                        },
                        {
                            "id": "10203319736891580",
                            "name": "Jim Verschooten",
                            "type": "LIKE"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "TVRVNE9EZA3dNek00TURveE5EZA3pNemMyT1RJek9qSTFOREE1TmpFMk1UTT0ZD",
                            "after": "TVRFMU5URTROakV4TmpveE5EZA3pNamM1TURFeE9qSTFOREE1TmpFMk1UTT0ZD"
                        }
                    }
                },
                "likes": {
                    "data": [
                        {
                            "id": "10205642438252116",
                            "name": "Rombauts Liliane"
                        },
                        {
                            "id": "10200799741795383",
                            "name": "Kristel Andries"
                        },
                        {
                            "id": "777088352349300",
                            "name": "Karin Derua"
                        },
                        {
                            "id": "10203468894942478",
                            "name": "Ilse Fillet"
                        },
                        {
                            "id": "623417957794168",
                            "name": "Mariette Van Noten"
                        },
                        {
                            "id": "131618487010457",
                            "name": "Open VLD Haacht"
                        },
                        {
                            "id": "10203319736891580",
                            "name": "Jim Verschooten"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "MTAyMDU2NDI0MzgyNTIxMTYZD",
                            "after": "MTAyMDMzMTk3MzY4OTE1ODAZD"
                        }
                    }
                }
            },
            {
                "from": {
                    "name": "Open Vld Hoegaarden",
                    "id": "259090000812704"
                },
                "created_time": "2017-01-01T11:38:28+0000",
                "description": "Beste wensen voor 2017! Open Vld wenst je een jaar vol vrijheid.",
                "id": "259090000812704_1197509636970731",
                "story": "Open Vld Hoegaarden shared Open Vld's photo.",
                "type": "photo",
                "reactions": {
                    "data": [
                        {
                            "id": "1815320545373820",
                            "name": "Marlien van Lierde",
                            "type": "LIKE"
                        },
                        {
                            "id": "10152439825857213",
                            "name": "Lode Vereeck",
                            "type": "LIKE"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "TVRBd01EQTJPRGMyTnpZAM05UVTRPakUwT0RNeU56WTRNekk2TWpVME1EazJNVFl4TXc9PQZDZD",
                            "after": "TmpFME5EZAzNNakV5T2pFME9ETXlOek15TWpFNk1qVTBNRGsyTVRZAeE13PT0ZD"
                        }
                    }
                },
                "likes": {
                    "data": [
                        {
                            "id": "1815320545373820",
                            "name": "Marlien van Lierde"
                        },
                        {
                            "id": "10152439825857213",
                            "name": "Lode Vereeck"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "MTgxNTMyMDU0NTM3MzgyMAZDZD",
                            "after": "MTAxNTI0Mzk4MjU4NTcyMTMZD"
                        }
                    }
                }
            },
            {
                "from": {
                    "name": "Open VLD Dilbeek",
                    "id": "777204709088449"
                },
                "created_time": "2017-01-01T11:10:53+0000",
                "description": "Beste wensen voor 2017! Open Vld wenst je een jaar vol vrijheid.",
                "id": "777204709088449_888181421324110",
                "story": "Open VLD Dilbeek shared Open Vld's photo.",
                "type": "photo",
                "reactions": {
                    "data": [
                        {
                            "id": "10203895896191357",
                            "name": "Christiane De Groodt",
                            "type": "LIKE"
                        },
                        {
                            "id": "10205970135210851",
                            "name": "Stephane Evenepoel",
                            "type": "LIKE"
                        },
                        {
                            "id": "1522709414659814",
                            "name": "Liliane Jacobs",
                            "type": "LIKE"
                        },
                        {
                            "id": "1241795322501217",
                            "name": "Bart Nevens",
                            "type": "LIKE"
                        },
                        {
                            "id": "947567488620126",
                            "name": "Sofie Verweire",
                            "type": "LIKE"
                        },
                        {
                            "id": "10211410511081050",
                            "name": "Stefan Muylaert",
                            "type": "LIKE"
                        },
                        {
                            "id": "10205340828907543",
                            "name": "Joseph Walravens",
                            "type": "LIKE"
                        },
                        {
                            "id": "609483639178694",
                            "name": "Wauters Willy",
                            "type": "LIKE"
                        },
                        {
                            "id": "1194033147354436",
                            "name": "Ronny Van Linthout",
                            "type": "LIKE"
                        },
                        {
                            "id": "10203755392911252",
                            "name": "Olivier Cranskens",
                            "type": "LIKE"
                        },
                        {
                            "id": "455932481269112",
                            "name": "Bart Scholliers",
                            "type": "LIKE"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "TVRZAek9UZAzFOell3TmpveE5EZAzBOakExTWpBMk9qSTFOREE1TmpFMk1UTT0ZD",
                            "after": "TVRBd01EQTFOVGN3T1RFM01URXdPakUwT0RNeU5qa3hOVGM2TWpVME1EazJNVFl4TXc9PQZDZD"
                        }
                    }
                },
                "likes": {
                    "data": [
                        {
                            "id": "10203895896191357",
                            "name": "Christiane De Groodt"
                        },
                        {
                            "id": "10205970135210851",
                            "name": "Stephane Evenepoel"
                        },
                        {
                            "id": "1522709414659814",
                            "name": "Liliane Jacobs"
                        },
                        {
                            "id": "1241795322501217",
                            "name": "Bart Nevens"
                        },
                        {
                            "id": "947567488620126",
                            "name": "Sofie Verweire"
                        },
                        {
                            "id": "10211410511081050",
                            "name": "Stefan Muylaert"
                        },
                        {
                            "id": "10205340828907543",
                            "name": "Joseph Walravens"
                        },
                        {
                            "id": "609483639178694",
                            "name": "Wauters Willy"
                        },
                        {
                            "id": "1194033147354436",
                            "name": "Ronny Van Linthout"
                        },
                        {
                            "id": "10203755392911252",
                            "name": "Olivier Cranskens"
                        },
                        {
                            "id": "455932481269112",
                            "name": "Bart Scholliers"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "MTAyMDM4OTU4OTYxOTEzNTcZD",
                            "after": "NDU1OTMyNDgxMjY5MTEy"
                        }
                    }
                }
            },
            {
                "from": {
                    "name": "Olivier Lesceu",
                    "id": "850368334978417"
                },
                "created_time": "2017-01-01T10:00:00+0000",
                "description": "Beste wensen voor 2017! Open Vld wenst je een jaar vol vrijheid.",
                "id": "850368334978417_1585011868180723",
                "message": "Open VLD Beersel wenst u en uw familie een gezond en overweldigend 2016!!!",
                "story": "Olivier Lesceu shared Open Vld's photo in Beersel.",
                "type": "photo",
                "reactions": {
                    "data": [
                        {
                            "id": "10202842564944579",
                            "name": "Josette Harnie",
                            "type": "LIKE"
                        },
                        {
                            "id": "10207883935842490",
                            "name": "Lieve Van Cotthem",
                            "type": "LIKE"
                        },
                        {
                            "id": "810582295694299",
                            "name": "Olivier Lesceu",
                            "type": "LIKE"
                        },
                        {
                            "id": "439157419437602",
                            "name": "Open Vld Beersel",
                            "type": "LIKE"
                        },
                        {
                            "id": "10204469866200480",
                            "name": "Catherine Bernard",
                            "type": "LIKE"
                        },
                        {
                            "id": "850368334978417",
                            "name": "Olivier Lesceu",
                            "type": "LIKE"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "TVRneE5URTVOakV4TVRveE5EZA3pNelEzTXpRNE9qSTFOREE1TmpFMk1UTT0ZD",
                            "after": "T0RVd016WTRNek0wT1RjNE5ERTNPakUwT0RNeU9ETTRNelk2TWpVME1EazJNVFl4TXc9PQZDZD"
                        }
                    }
                },
                "likes": {
                    "data": [
                        {
                            "id": "10202842564944579",
                            "name": "Josette Harnie"
                        },
                        {
                            "id": "10207883935842490",
                            "name": "Lieve Van Cotthem"
                        },
                        {
                            "id": "810582295694299",
                            "name": "Olivier Lesceu"
                        },
                        {
                            "id": "439157419437602",
                            "name": "Open Vld Beersel"
                        },
                        {
                            "id": "10204469866200480",
                            "name": "Catherine Bernard"
                        },
                        {
                            "id": "850368334978417",
                            "name": "Olivier Lesceu"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "MTAyMDI4NDI1NjQ5NDQ1NzkZD",
                            "after": "ODUwMzY4MzM0OTc4NDE3"
                        }
                    }
                }
            },
            {
                "from": {
                    "name": "Open Vld Beersel",
                    "id": "439157419437602"
                },
                "created_time": "2017-01-01T09:00:00+0000",
                "description": "Beste wensen voor 2017! Open Vld wenst je een jaar vol vrijheid.",
                "id": "439157419437602_1364457016907633",
                "message": "Open VLD Beersel wenst u en uw familie een gezond en overweldigend 2017!!!",
                "story": "Open Vld Beersel shared Open Vld's photo  in Beersel.",
                "type": "photo",
                "reactions": {
                    "data": [
                        {
                            "id": "1858298587783006",
                            "name": "Agnes Deceuninck",
                            "type": "LIKE"
                        },
                        {
                            "id": "810582295694299",
                            "name": "Olivier Lesceu",
                            "type": "LIKE"
                        },
                        {
                            "id": "10153646704184743",
                            "name": "Anthony Kreveld",
                            "type": "LIKE"
                        },
                        {
                            "id": "850368334978417",
                            "name": "Olivier Lesceu",
                            "type": "LIKE"
                        },
                        {
                            "id": "10204469866200480",
                            "name": "Catherine Bernard",
                            "type": "LIKE"
                        },
                        {
                            "id": "439157419437602",
                            "name": "Open Vld Beersel",
                            "type": "LIKE"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "TVRBd01EQTRNRGcyTkRnM056TTVPakUwT0RNek1EYzNOamc2TWpVME1EazJNVFl4TXc9PQZDZD",
                            "after": "TkRNNU1UVTNOREU1TkRNM05qQXlPakUwT0RNeU9ETTNNVFE2TWpVME1EazJNVFl4TXc9PQZDZD"
                        }
                    }
                },
                "likes": {
                    "data": [
                        {
                            "id": "1858298587783006",
                            "name": "Agnes Deceuninck"
                        },
                        {
                            "id": "810582295694299",
                            "name": "Olivier Lesceu"
                        },
                        {
                            "id": "10153646704184743",
                            "name": "Anthony Kreveld"
                        },
                        {
                            "id": "850368334978417",
                            "name": "Olivier Lesceu"
                        },
                        {
                            "id": "10204469866200480",
                            "name": "Catherine Bernard"
                        },
                        {
                            "id": "439157419437602",
                            "name": "Open Vld Beersel"
                        }
                    ],
                    "paging": {
                        "cursors": {
                            "before": "MTg1ODI5ODU4Nzc4MzAwNgZDZD",
                            "after": "NDM5MTU3NDE5NDM3NjAy"
                        }
                    }
                }
            }
        ],
        "paging": {
            "cursors": {
                "after": "ODg4MTgxNDIxMzI0MTEw",
                "before": "ODMwMzM3NjgwNDAyNzg1"
            }
        }
    }
}

xu = convert2unicode(x)
print x == xu

pprint(x['comments'])
pprint(xu['comments'])

post.comments = xu['comments']

post.save(validate=False, force_insert=False)

# ps = FbPost.objects
# for p in ps:
#     print type(p), p
#     print p.comments
#
#     # p.comments = 23
#     # p.save()

pass

# FbPost_Realistic_Factory.create_batch(1)
