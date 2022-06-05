import nltk
from nltk.util import bigrams
import numpy as np
from scipy.linalg import svd
from numpy import linalg
corpus = '''
THE GODS IN COUNCIL—MINERVA’S VISIT TO ITHACA—THE CHALLENGE FROM
TELEMACHUS TO THE SUITORS.


Tell me, O Muse, of that ingenious hero who travelled far and wide
after he had sacked the famous town of Troy. Many cities did he visit,
and many were the nations with whose manners and customs he was
acquainted; moreover he suffered much by sea while trying to save his
own life and bring his men safely home; but do what he might he could
not save his men, for they perished through their own sheer folly in
eating the cattle of the Sun-god Hyperion; so the god prevented them
from ever reaching home. Tell me, too, about all these things, oh
daughter of Jove, from whatsoever source you may know them.

So now all who escaped death in battle or by shipwreck had got safely
home except Ulysses, and he, though he was longing to return to his
wife and country, was detained by the goddess Calypso, who had got him
into a large cave and wanted to marry him. But as years went by, there
came a time when the gods settled that he should go back to Ithaca;
even then, however, when he was among his own people, his troubles were
not yet over; nevertheless all the gods had now begun to pity him
except Neptune, who still persecuted him without ceasing and would not
let him get home.

Now Neptune had gone off to the Ethiopians, who are at the world’s end,
and lie in two halves, the one looking West and the other East.1 He had
gone there to accept a hecatomb of sheep and oxen, and was enjoying
himself at his festival; but the other gods met in the house of
Olympian Jove, and the sire of gods and men spoke first. At that moment
he was thinking of Aegisthus, who had been killed by Agamemnon’s son
Orestes; so he said to the other gods:

“See now, how men lay blame upon us gods for what is after all nothing
but their own folly. Look at Aegisthus; he must needs make love to
Agamemnon’s wife unrighteously and then kill Agamemnon, though he knew
it would be the death of him; for I sent Mercury to warn him not to do
either of these things, inasmuch as Orestes would be sure to take his
revenge when he grew up and wanted to return home. Mercury told him
this in all good will but he would not listen, and now he has paid for
everything in full.”

Then Minerva said, “Father, son of Saturn, King of kings, it served
Aegisthus right, and so it would any one else who does as he did; but
Aegisthus is neither here nor there; it is for Ulysses that my heart
bleeds, when I think of his sufferings in that lonely sea-girt island,
far away, poor man, from all his friends. It is an island covered with
forest, in the very middle of the sea, and a goddess lives there,
daughter of the magician Atlas, who looks after the bottom of the
ocean, and carries the great columns that keep heaven and earth
asunder. This daughter of Atlas has got hold of poor unhappy Ulysses,
and keeps trying by every kind of blandishment to make him forget his
home, so that he is tired of life, and thinks of nothing but how he may
once more see the smoke of his own chimneys. You, sir, take no heed of
this, and yet when Ulysses was before Troy did he not propitiate you
with many a burnt sacrifice? Why then should you keep on being so angry
with him?”

And Jove said, “My child, what are you talking about? How can I forget
Ulysses than whom there is no more capable man on earth, nor more
liberal in his offerings to the immortal gods that live in heaven? Bear
in mind, however, that Neptune is still furious with Ulysses for having
blinded an eye of Polyphemus king of the Cyclopes. Polyphemus is son to
Neptune by the nymph Thoosa, daughter to the sea-king Phorcys;
therefore though he will not kill Ulysses outright, he torments him by
preventing him from getting home. Still, let us lay our heads together
and see how we can help him to return; Neptune will then be pacified,
for if we are all of a mind he can hardly stand out against us.”

And Minerva said, “Father, son of Saturn, King of kings, if, then, the
gods now mean that Ulysses should get home, we should first send
Mercury to the Ogygian island to tell Calypso that we have made up our
minds and that he is to return. In the meantime I will go to Ithaca, to
put heart into Ulysses’ son Telemachus; I will embolden him to call the
Achaeans in assembly, and speak out to the suitors of his mother
Penelope, who persist in eating up any number of his sheep and oxen; I
will also conduct him to Sparta and to Pylos, to see if he can hear
anything about the return of his dear father—for this will make people
speak well of him.”

So saying she bound on her glittering golden sandals, imperishable,
with which she can fly like the wind over land or sea; she grasped the
redoubtable bronze-shod spear, so stout and sturdy and strong,
wherewith she quells the ranks of heroes who have displeased her, and
down she darted from the topmost summits of Olympus, whereon forthwith
she was in Ithaca, at the gateway of Ulysses’ house, disguised as a
visitor, Mentes, chief of the Taphians, and she held a bronze spear in
her hand. There she found the lordly suitors seated on hides of the
oxen which they had killed and eaten, and playing draughts in front of
the house. Men-servants and pages were bustling about to wait upon
them, some mixing wine with water in the mixing-bowls, some cleaning
down the tables with wet sponges and laying them out again, and some
cutting up great quantities of meat.

Telemachus saw her long before any one else did. He was sitting moodily
among the suitors thinking about his brave father, and how he would
send them flying out of the house, if he were to come to his own again
and be honoured as in days gone by. Thus brooding as he sat among them,
he caught sight of Minerva and went straight to the gate, for he was
vexed that a stranger should be kept waiting for admittance. He took
her right hand in his own, and bade her give him her spear. “Welcome,”
said he, “to our house, and when you have partaken of food you shall
tell us what you have come for.”

He led the way as he spoke, and Minerva followed him. When they were
within he took her spear and set it in the spear-stand against a strong
bearing-post along with the many other spears of his unhappy father,
and he conducted her to a richly decorated seat under which he threw a
cloth of damask. There was a footstool also for her feet,2 and he set
another seat near her for himself, away from the suitors, that she
might not be annoyed while eating by their noise and insolence, and
that he might ask her more freely about his father.

A maid servant then brought them water in a beautiful golden ewer and
poured it into a silver basin for them to wash their hands, and she
drew a clean table beside them. An upper servant brought them bread,
and offered them many good things of what there was in the house, the
carver fetched them plates of all manner of meats and set cups of gold
by their side, and a manservant brought them wine and poured it out for
them.


Then the suitors came in and took their places on the benches and
seats.3 Forthwith men servants poured water over their hands, maids
went round with the bread-baskets, pages filled the mixing-bowls with
wine and water, and they laid their hands upon the good things that
were before them. As soon as they had had enough to eat and drink they
wanted music and dancing, which are the crowning embellishments of a
banquet, so a servant brought a lyre to Phemius, whom they compelled
perforce to sing to them. As soon as he touched his lyre and began to
sing Telemachus spoke low to Minerva, with his head close to hers that
no man might hear.

“I hope, sir,” said he, “that you will not be offended with what I am
going to say. Singing comes cheap to those who do not pay for it, and
all this is done at the cost of one whose bones lie rotting in some
wilderness or grinding to powder in the surf. If these men were to see
my father come back to Ithaca they would pray for longer legs rather
than a longer purse, for money would not serve them; but he, alas, has
fallen on an ill fate, and even when people do sometimes say that he is
coming, we no longer heed them; we shall never see him again. And now,
sir, tell me and tell me true, who you are and where you come from.
Tell me of your town and parents, what manner of ship you came in, how
your crew brought you to Ithaca, and of what nation they declared
themselves to be—for you cannot have come by land. Tell me also truly,
for I want to know, are you a stranger to this house, or have you been
here in my father’s time? In the old days we had many visitors for my
father went about much himself.”

And Minerva answered, “I will tell you truly and particularly all about
it. I am Mentes, son of Anchialus, and I am King of the Taphians. I
have come here with my ship and crew, on a voyage to men of a foreign
tongue being bound for Temesa4 with a cargo of iron, and I shall bring
back copper. As for my ship, it lies over yonder off the open country
away from the town, in the harbour Rheithron5 under the wooded mountain
Neritum.6 Our fathers were friends before us, as old Laertes will tell
you, if you will go and ask him. They say, however, that he never comes
to town now, and lives by himself in the country, faring hardly, with
an old woman to look after him and get his dinner for him, when he
comes in tired from pottering about his vineyard. They told me your
father was at home again, and that was why I came, but it seems the
gods are still keeping him back, for he is not dead yet not on the
mainland. It is more likely he is on some sea-girt island in mid ocean,
or a prisoner among savages who are detaining him against his will. I
am no prophet, and know very little about omens, but I speak as it is
borne in upon me from heaven, and assure you that he will not be away
much longer; for he is a man of such resource that even though he were
in chains of iron he would find some means of getting home again. But
tell me, and tell me true, can Ulysses really have such a fine looking
fellow for a son? You are indeed wonderfully like him about the head
and eyes, for we were close friends before he set sail for Troy where
the flower of all the Argives went also. Since that time we have never
either of us seen the other.”

“My mother,” answered Telemachus, “tells me I am son to Ulysses, but it
is a wise child that knows his own father. Would that I were son to one
who had grown old upon his own estates, for, since you ask me, there is
no more ill-starred man under heaven than he who they tell me is my
father.”

And Minerva said, “There is no fear of your race dying out yet, while
Penelope has such a fine son as you are. But tell me, and tell me true,
what is the meaning of all this feasting, and who are these people?
What is it all about? Have you some banquet, or is there a wedding in
the family—for no one seems to be bringing any provisions of his own?
And the guests—how atrociously they are behaving; what riot they make
over the whole house; it is enough to disgust any respectable person
who comes near them.”

“Sir,” said Telemachus, “as regards your question, so long as my father
was here it was well with us and with the house, but the gods in their
displeasure have willed it otherwise, and have hidden him away more
closely than mortal man was ever yet hidden. I could have borne it
better even though he were dead, if he had fallen with his men before
Troy, or had died with friends around him when the days of his fighting
were done; for then the Achaeans would have built a mound over his
ashes, and I should myself have been heir to his renown; but now the
storm-winds have spirited him away we know not whither; he is gone
without leaving so much as a trace behind him, and I inherit nothing
but dismay. Nor does the matter end simply with grief for the loss of
my father; heaven has laid sorrows upon me of yet another kind; for the
chiefs from all our islands, Dulichium, Same, and the woodland island
of Zacynthus, as also all the principal men of Ithaca itself, are
eating up my house under the pretext of paying their court to my
mother, who will neither point blank say that she will not marry,7 nor
yet bring matters to an end; so they are making havoc of my estate, and
before long will do so also with myself.”

“Is that so?” exclaimed Minerva, “then you do indeed want Ulysses home
again. Give him his helmet, shield, and a couple of lances, and if he
is the man he was when I first knew him in our house, drinking and
making merry, he would soon lay his hands about these rascally suitors,
were he to stand once more upon his own threshold. He was then coming
from Ephyra, where he had been to beg poison for his arrows from Ilus,
son of Mermerus. Ilus feared the ever-living gods and would not give
him any, but my father let him have some, for he was very fond of him.
If Ulysses is the man he then was these suitors will have a short
shrift and a sorry wedding.

“But there! It rests with heaven to determine whether he is to return,
and take his revenge in his own house or no; I would, however, urge you
to set about trying to get rid of these suitors at once. Take my
advice, call the Achaean heroes in assembly to-morrow morning—lay your
case before them, and call heaven to bear you witness. Bid the suitors
take themselves off, each to his own place, and if your mother’s mind
is set on marrying again, let her go back to her father, who will find
her a husband and provide her with all the marriage gifts that so dear
a daughter may expect. As for yourself, let me prevail upon you to take
the best ship you can get, with a crew of twenty men, and go in quest
of your father who has so long been missing. Some one may tell you
something, or (and people often hear things in this way) some
heaven-sent message may direct you. First go to Pylos and ask Nestor;
thence go on to Sparta and visit Menelaus, for he got home last of all
the Achaeans; if you hear that your father is alive and on his way
home, you can put up with the waste these suitors will make for yet
another twelve months. If on the other hand you hear of his death, come
home at once, celebrate his funeral rites with all due pomp, build a
barrow to his memory, and make your mother marry again. Then, having
done all this, think it well over in your mind how, by fair means or
foul, you may kill these suitors in your own house. You are too old to
plead infancy any longer; have you not heard how people are singing
Orestes’ praises for having killed his father’s murderer Aegisthus? You
are a fine, smart looking fellow; show your mettle, then, and make
yourself a name in story. Now, however, I must go back to my ship and
to my crew, who will be impatient if I keep them waiting longer; think
the matter over for yourself, and remember what I have said to you.”

“Sir,” answered Telemachus, “it has been very kind of you to talk to me
in this way, as though I were your own son, and I will do all you tell
me; I know you want to be getting on with your voyage, but stay a
little longer till you have taken a bath and refreshed yourself. I will
then give you a present, and you shall go on your way rejoicing; I will
give you one of great beauty and value—a keepsake such as only dear
friends give to one another.”

Minerva answered, “Do not try to keep me, for I would be on my way at
once. As for any present you may be disposed to make me, keep it till I
come again, and I will take it home with me. You shall give me a very
good one, and I will give you one of no less value in return.”

With these words she flew away like a bird into the air, but she had
given Telemachus courage, and had made him think more than ever about
his father. He felt the change, wondered at it, and knew that the
stranger had been a god, so he went straight to where the suitors were
sitting.

Phemius was still singing, and his hearers sat rapt in silence as he
told the sad tale of the return from Troy, and the ills Minerva had
laid upon the Achaeans. Penelope, daughter of Icarius, heard his song
from her room upstairs, and came down by the great staircase, not
alone, but attended by two of her handmaids. When she reached the
suitors she stood by one of the bearing posts that supported the roof
of the cloisters8 with a staid maiden on either side of her. She held a
veil, moreover, before her face, and was weeping bitterly.

“Phemius,” she cried, “you know many another feat of gods and heroes,
such as poets love to celebrate. Sing the suitors some one of these,
and let them drink their wine in silence, but cease this sad tale, for
it breaks my sorrowful heart, and reminds me of my lost husband whom I
mourn ever without ceasing, and whose name was great over all Hellas
and middle Argos.”9

“Mother,” answered Telemachus, “let the bard sing what he has a mind
to; bards do not make the ills they sing of; it is Jove, not they, who
makes them, and who sends weal or woe upon mankind according to his own
good pleasure. This fellow means no harm by singing the ill-fated
return of the Danaans, for people always applaud the latest songs most
warmly. Make up your mind to it and bear it; Ulysses is not the only
man who never came back from Troy, but many another went down as well
as he. Go, then, within the house and busy yourself with your daily
duties, your loom, your distaff, and the ordering of your servants; for
speech is man’s matter, and mine above all others 10—for it is I who am
master here.”

She went wondering back into the house, and laid her son’s saying in
her heart. Then, going upstairs with her handmaids into her room, she
mourned her dear husband till Minerva shed sweet sleep over her eyes.
But the suitors were clamorous throughout the covered cloisters11, and
prayed each one that he might be her bed fellow.

Then Telemachus spoke, “Shameless,” he cried, “and insolent suitors,
let us feast at our pleasure now, and let there be no brawling, for it
is a rare thing to hear a man with such a divine voice as Phemius has;
but in the morning meet me in full assembly that I may give you formal
notice to depart, and feast at one another’s houses, turn and turn
about, at your own cost. If on the other hand you choose to persist in
spunging upon one man, heaven help me, but Jove shall reckon with you
in full, and when you fall in my father’s house there shall be no man
to avenge you.”

The suitors bit their lips as they heard him, and marvelled at the
boldness of his speech. Then, Antinous, son of Eupeithes, said, “The
gods seem to have given you lessons in bluster and tall talking; may
Jove never grant you to be chief in Ithaca as your father was before
you.”

Telemachus answered, “Antinous, do not chide with me, but, god willing,
I will be chief too if I can. Is this the worst fate you can think of
for me? It is no bad thing to be a chief, for it brings both riches and
honour. Still, now that Ulysses is dead there are many great men in
Ithaca both old and young, and some other may take the lead among them;
nevertheless I will be chief in my own house, and will rule those whom
Ulysses has won for me.”

Then Eurymachus, son of Polybus, answered, “It rests with heaven to
decide who shall be chief among us, but you shall be master in your own
house and over your own possessions; no one while there is a man in
Ithaca shall do you violence nor rob you. And now, my good fellow, I
want to know about this stranger. What country does he come from? Of
what family is he, and where is his estate? Has he brought you news
about the return of your father, or was he on business of his own? He
seemed a well to do man, but he hurried off so suddenly that he was
gone in a moment before we could get to know him.”

“My father is dead and gone,” answered Telemachus, “and even if some
rumour reaches me I put no more faith in it now. My mother does indeed
sometimes send for a soothsayer and question him, but I give his
prophecyings no heed. As for the stranger, he was Mentes, son of
Anchialus, chief of the Taphians, an old friend of my father’s.” But in
his heart he knew that it had been the goddess.

The suitors then returned to their singing and dancing until the
evening; but when night fell upon their pleasuring they went home to
bed each in his own abode.12 Telemachus’s room was high up in a tower13
that looked on to the outer court; hither, then, he hied, brooding and
full of thought. A good old woman, Euryclea, daughter of Ops, the son
of Pisenor, went before him with a couple of blazing torches. Laertes
had bought her with his own money when she was quite young; he gave the
worth of twenty oxen for her, and shewed as much respect to her in his
household as he did to his own wedded wife, but he did not take her to
his bed for he feared his wife’s resentment.14 She it was who now
lighted Telemachus to his room, and she loved him better than any of
the other women in the house did, for she had nursed him when he was a
baby. He opened the door of his bed room and sat down upon the bed; as
he took off his shirt15 he gave it to the good old woman, who folded it
tidily up, and hung it for him over a peg by his bed side, after which
she went out, pulled the door to by a silver catch, and drew the bolt
home by means of the strap.16 But Telemachus as he lay covered with a
woollen fleece kept thinking all night through of his intended voyage
and of the counsel that Minerva had given him.






Now when the child of morning, rosy-fingered Dawn, appeared Telemachus
rose and dressed himself. He bound his sandals on to his comely feet,
girded his sword about his shoulder, and left his room looking like an
immortal god. He at once sent the criers round to call the people in
assembly, so they called them and the people gathered thereon; then,
when they were got together, he went to the place of assembly spear in
hand—not alone, for his two hounds went with him. Minerva endowed him
with a presence of such divine comeliness that all marvelled at him as
he went by, and when he took his place in his father’s seat even the
oldest councillors made way for him.

Aegyptius, a man bent double with age, and of infinite experience, was
the first to speak. His son Antiphus had gone with Ulysses to Ilius,
land of noble steeds, but the savage Cyclops had killed him when they
were all shut up in the cave, and had cooked his last dinner for him.17
He had three sons left, of whom two still worked on their father’s
land, while the third, Eurynomus, was one of the suitors; nevertheless
their father could not get over the loss of Antiphus, and was still
weeping for him when he began his speech.

“Men of Ithaca,” he said, “hear my words. From the day Ulysses left us
there has been no meeting of our councillors until now; who then can it
be, whether old or young, that finds it so necessary to convene us? Has
he got wind of some host approaching, and does he wish to warn us, or
would he speak upon some other matter of public moment? I am sure he is
an excellent person, and I hope Jove will grant him his heart’s
desire.”

Telemachus took this speech as of good omen and rose at once, for he
was bursting with what he had to say. He stood in the middle of the
assembly and the good herald Pisenor brought him his staff. Then,
turning to Aegyptius, “Sir,” said he, “it is I, as you will shortly
learn, who have convened you, for it is I who am the most aggrieved. I
have not got wind of any host approaching about which I would warn you,
nor is there any matter of public moment on which I would speak. My
grievance is purely personal, and turns on two great misfortunes which
have fallen upon my house. The first of these is the loss of my
excellent father, who was chief among all you here present, and was
like a father to every one of you; the second is much more serious, and
ere long will be the utter ruin of my estate. The sons of all the chief
men among you are pestering my mother to marry them against her will.
They are afraid to go to her father Icarius, asking him to choose the
one he likes best, and to provide marriage gifts for his daughter, but
day by day they keep hanging about my father’s house, sacrificing our
oxen, sheep, and fat goats for their banquets, and never giving so much
as a thought to the quantity of wine they drink. No estate can stand
such recklessness; we have now no Ulysses to ward off harm from our
doors, and I cannot hold my own against them. I shall never all my days
be as good a man as he was, still I would indeed defend myself if I had
power to do so, for I cannot stand such treatment any longer; my house
is being disgraced and ruined. Have respect, therefore, to your own
consciences and to public opinion. Fear, too, the wrath of heaven, lest
the gods should be displeased and turn upon you. I pray you by Jove and
Themis, who is the beginning and the end of councils, [do not] hold
back, my friends, and leave me singlehanded18—unless it be that my
brave father Ulysses did some wrong to the Achaeans which you would now
avenge on me, by aiding and abetting these suitors. Moreover, if I am
to be eaten out of house and home at all, I had rather you did the
eating yourselves, for I could then take action against you to some
purpose, and serve you with notices from house to house till I got paid
in full, whereas now I have no remedy.”19

With this Telemachus dashed his staff to the ground and burst into
tears. Every one was very sorry for him, but they all sat still and no
one ventured to make him an angry answer, save only Antinous, who spoke
thus:

“Telemachus, insolent braggart that you are, how dare you try to throw
the blame upon us suitors? It is your mother’s fault not ours, for she
is a very artful woman. This three years past, and close on four, she
had been driving us out of our minds, by encouraging each one of us,
and sending him messages without meaning one word of what she says. And
then there was that other trick she played us. She set up a great
tambour frame in her room, and began to work on an enormous piece of
fine needlework. ‘Sweet hearts,’ said she, ‘Ulysses is indeed dead,
still do not press me to marry again immediately, wait—for I would not
have skill in needlework perish unrecorded—till I have completed a pall
for the hero Laertes, to be in readiness against the time when death
shall take him. He is very rich, and the women of the place will talk
if he is laid out without a pall.’

“This was what she said, and we assented; whereon we could see her
working on her great web all day long, but at night she would unpick
the stitches again by torchlight. She fooled us in this way for three
years and we never found her out, but as time wore on and she was now
in her fourth year, one of her maids who knew what she was doing told
us, and we caught her in the act of undoing her work, so she had to
finish it whether she would or no. The suitors, therefore, make you
this answer, that both you and the Achaeans may understand—‘Send your
mother away, and bid her marry the man of her own and of her father’s
choice’; for I do not know what will happen if she goes on plaguing us
much longer with the airs she gives herself on the score of the
accomplishments Minerva has taught her, and because she is so clever.
We never yet heard of such a woman; we know all about Tyro, Alcmena,
Mycene, and the famous women of old, but they were nothing to your
mother any one of them. It was not fair of her to treat us in that way,
and as long as she continues in the mind with which heaven has now
endowed her, so long shall we go on eating up your estate; and I do not
see why she should change, for she gets all the honour and glory, and
it is you who pay for it, not she. Understand, then, that we will not
go back to our lands, neither here nor elsewhere, till she has made her
choice and married some one or other of us.”

Telemachus answered, “Antinous, how can I drive the mother who bore me
from my father’s house? My father is abroad and we do not know whether
he is alive or dead. It will be hard on me if I have to pay Icarius the
large sum which I must give him if I insist on sending his daughter
back to him. Not only will he deal rigorously with me, but heaven will
also punish me; for my mother when she leaves the house will call on
the Erinyes to avenge her; besides, it would not be a creditable thing
to do, and I will have nothing to say to it. If you choose to take
offence at this, leave the house and feast elsewhere at one another’s
houses at your own cost turn and turn about. If, on the other hand, you
elect to persist in spunging upon one man, heaven help me, but Jove
shall reckon with you in full, and when you fall in my father’s house
there shall be no man to avenge you.”

As he spoke Jove sent two eagles from the top of the mountain, and they
flew on and on with the wind, sailing side by side in their own lordly
flight. When they were right over the middle of the assembly they
wheeled and circled about, beating the air with their wings and glaring
death into the eyes of them that were below; then, fighting fiercely
and tearing at one another, they flew off towards the right over the
town. The people wondered as they saw them, and asked each other what
all this might be; whereon Halitherses, who was the best prophet and
reader of omens among them, spoke to them plainly and in all honesty,
saying:

“Hear me, men of Ithaca, and I speak more particularly to the suitors,
for I see mischief brewing for them. Ulysses is not going to be away
much longer; indeed he is close at hand to deal out death and
destruction, not on them alone, but on many another of us who live in
Ithaca. Let us then be wise in time, and put a stop to this wickedness
before he comes. Let the suitors do so of their own accord; it will be
better for them, for I am not prophesying without due knowledge;
everything has happened to Ulysses as I foretold when the Argives set
out for Troy, and he with them. I said that after going through much
hardship and losing all his men he should come home again in the
twentieth year and that no one would know him; and now all this is
coming true.”

Eurymachus son of Polybus then said, “Go home, old man, and prophesy to
your own children, or it may be worse for them. I can read these omens
myself much better than you can; birds are always flying about in the
sunshine somewhere or other, but they seldom mean anything. Ulysses has
died in a far country, and it is a pity you are not dead along with
him, instead of prating here about omens and adding fuel to the anger
of Telemachus which is fierce enough as it is. I suppose you think he
will give you something for your family, but I tell you—and it shall
surely be—when an old man like you, who should know better, talks a
young one over till he becomes troublesome, in the first place his
young friend will only fare so much the worse—he will take nothing by
it, for the suitors will prevent this—and in the next, we will lay a
heavier fine, sir, upon yourself than you will at all like paying, for
it will bear hardly upon you. As for Telemachus, I warn him in the
presence of you all to send his mother back to her father, who will
find her a husband and provide her with all the marriage gifts so dear
a daughter may expect. Till then we shall go on harassing him with our
suit; for we fear no man, and care neither for him, with all his fine
speeches, nor for any fortune-telling of yours. You may preach as much
as you please, but we shall only hate you the more. We shall go back
and continue to eat up Telemachus’s estate without paying him, till
such time as his mother leaves off tormenting us by keeping us day
after day on the tiptoe of expectation, each vying with the other in
his suit for a prize of such rare perfection. Besides we cannot go
after the other women whom we should marry in due course, but for the
way in which she treats us.”

Then Telemachus said, “Eurymachus, and you other suitors, I shall say
no more, and entreat you no further, for the gods and the people of
Ithaca now know my story. Give me, then, a ship and a crew of twenty
men to take me hither and thither, and I will go to Sparta and to Pylos
in quest of my father who has so long been missing. Some one may tell
me something, or (and people often hear things in this way) some
heaven-sent message may direct me. If I can hear of him as alive and on
his way home I will put up with the waste you suitors will make for yet
another twelve months. If on the other hand I hear of his death, I will
return at once, celebrate his funeral rites with all due pomp, build a
barrow to his memory, and make my mother marry again.”

With these words he sat down, and Mentor20 who had been a friend of
Ulysses, and had been left in charge of everything with full authority
over the servants, rose to speak. He, then, plainly and in all honesty
addressed them thus:

“Hear me, men of Ithaca, I hope that you may never have a kind and
well-disposed ruler any more, nor one who will govern you equitably; I
hope that all your chiefs henceforward may be cruel and unjust, for
there is not one of you but has forgotten Ulysses, who ruled you as
though he were your father. I am not half so angry with the suitors,
for if they choose to do violence in the naughtiness of their hearts,
and wager their heads that Ulysses will not return, they can take the
high hand and eat up his estate, but as for you others I am shocked at
the way in which you all sit still without even trying to stop such
scandalous goings on—which you could do if you chose, for you are many
and they are few.”

Leiocritus, son of Evenor, answered him saying, “Mentor, what folly is
all this, that you should set the people to stay us? It is a hard thing
for one man to fight with many about his victuals. Even though Ulysses
himself were to set upon us while we are feasting in his house, and do
his best to oust us, his wife, who wants him back so very badly, would
have small cause for rejoicing, and his blood would be upon his own
head if he fought against such great odds. There is no sense in what
you have been saying. Now, therefore, do you people go about your
business, and let his father’s old friends, Mentor and Halitherses,
speed this boy on his journey, if he goes at all—which I do not think
he will, for he is more likely to stay where he is till some one comes
and tells him something.”

On this he broke up the assembly, and every man went back to his own
abode, while the suitors returned to the house of Ulysses.

Then Telemachus went all alone by the sea side, washed his hands in the
grey waves, and prayed to Minerva.

“Hear me,” he cried, “you god who visited me yesterday, and bade me
sail the seas in search of my father who has so long been missing. I
would obey you, but the Achaeans, and more particularly the wicked
suitors, are hindering me that I cannot do so.”

As he thus prayed, Minerva came close up to him in the likeness and
with the voice of Mentor. “Telemachus,” said she, “if you are made of
the same stuff as your father you will be neither fool nor coward
henceforward, for Ulysses never broke his word nor left his work half
done. If, then, you take after him, your voyage will not be fruitless,
but unless you have the blood of Ulysses and of Penelope in your veins
I see no likelihood of your succeeding. Sons are seldom as good men as
their fathers; they are generally worse, not better; still, as you are
not going to be either fool or coward henceforward, and are not
entirely without some share of your father’s wise discernment, I look
with hope upon your undertaking. But mind you never make common cause
with any of those foolish suitors, for they have neither sense nor
virtue, and give no thought to death and to the doom that will shortly
fall on one and all of them, so that they shall perish on the same day.
As for your voyage, it shall not be long delayed; your father was such
an old friend of mine that I will find you a ship, and will come with
you myself. Now, however, return home, and go about among the suitors;
begin getting provisions ready for your voyage; see everything well
stowed, the wine in jars, and the barley meal, which is the staff of
life, in leathern bags, while I go round the town and beat up
volunteers at once. There are many ships in Ithaca both old and new; I
will run my eye over them for you and will choose the best; we will get
her ready and will put out to sea without delay.”

Thus spoke Minerva daughter of Jove, and Telemachus lost no time in
doing as the goddess told him. He went moodily home, and found the
suitors flaying goats and singeing pigs in the outer court. Antinous
came up to him at once and laughed as he took his hand in his own,
saying, “Telemachus, my fine fire-eater, bear no more ill blood neither
in word nor deed, but eat and drink with us as you used to do. The
Achaeans will find you in everything—a ship and a picked crew to
boot—so that you can set sail for Pylos at once and get news of your
noble father.”

“Antinous,” answered Telemachus, “I cannot eat in peace, nor take
pleasure of any kind with such men as you are. Was it not enough that
you should waste so much good property of mine while I was yet a boy?
Now that I am older and know more about it, I am also stronger, and
whether here among this people, or by going to Pylos, I will do you all
the harm I can. I shall go, and my going will not be in vain—though,
thanks to you suitors, I have neither ship nor crew of my own, and must
be passenger not captain.”

As he spoke he snatched his hand from that of Antinous. Meanwhile the
others went on getting dinner ready about the buildings,21 jeering at
him tauntingly as they did so.

“Telemachus,” said one youngster, “means to be the death of us; I
suppose he thinks he can bring friends to help him from Pylos, or again
from Sparta, where he seems bent on going. Or will he go to Ephyra as
well, for poison to put in our wine and kill us?”

Another said, “Perhaps if Telemachus goes on board ship, he will be
like his father and perish far from his friends. In this case we should
have plenty to do, for we could then divide up his property amongst us:
as for the house we can let his mother and the man who marries her have
that.”

This was how they talked. But Telemachus went down into the lofty and
spacious store-room where his father’s treasure of gold and bronze lay
heaped up upon the floor, and where the linen and spare clothes were
kept in open chests. Here, too, there was a store of fragrant olive
oil, while casks of old, well-ripened wine, unblended and fit for a god
to drink, were ranged against the wall in case Ulysses should come home
again after all. The room was closed with well-made doors opening in
the middle; moreover the faithful old house-keeper Euryclea, daughter
of Ops the son of Pisenor, was in charge of everything both night and
day. Telemachus called her to the store-room and said:

“Nurse, draw me off some of the best wine you have, after what you are
keeping for my father’s own drinking, in case, poor man, he should
escape death, and find his way home again after all. Let me have twelve
jars, and see that they all have lids; also fill me some well-sewn
leathern bags with barley meal—about twenty measures in all. Get these
things put together at once, and say nothing about it. I will take
everything away this evening as soon as my mother has gone upstairs for
the night. I am going to Sparta and to Pylos to see if I can hear
anything about the return of my dear father.”

When Euryclea heard this she began to cry, and spoke fondly to him,
saying, “My dear child, what ever can have put such notion as that into
your head? Where in the world do you want to go to—you, who are the one
hope of the house? Your poor father is dead and gone in some foreign
country nobody knows where, and as soon as your back is turned these
wicked ones here will be scheming to get you put out of the way, and
will share all your possessions among themselves; stay where you are
among your own people, and do not go wandering and worrying your life
out on the barren ocean.”

“Fear not, nurse,” answered Telemachus, “my scheme is not without
heaven’s sanction; but swear that you will say nothing about all this
to my mother, till I have been away some ten or twelve days, unless she
hears of my having gone, and asks you; for I do not want her to spoil
her beauty by crying.”

The old woman swore most solemnly that she would not, and when she had
completed her oath, she began drawing off the wine into jars, and
getting the barley meal into the bags, while Telemachus went back to
the suitors.

Then Minerva bethought her of another matter. She took his shape, and
went round the town to each one of the crew, telling them to meet at
the ship by sundown. She went also to Noemon son of Phronius, and asked
him to let her have a ship—which he was very ready to do. When the sun
had set and darkness was over all the land, she got the ship into the
water, put all the tackle on board her that ships generally carry, and
stationed her at the end of the harbour. Presently the crew came up,
and the goddess spoke encouragingly to each of them.

Furthermore she went to the house of Ulysses, and threw the suitors
into a deep slumber. She caused their drink to fuddle them, and made
them drop their cups from their hands, so that instead of sitting over
their wine, they went back into the town to sleep, with their eyes
heavy and full of drowsiness. Then she took the form and voice of
Mentor, and called Telemachus to come outside.

“Telemachus,” said she, “the men are on board and at their oars,
waiting for you to give your orders, so make haste and let us be off.”

On this she led the way, while Telemachus followed in her steps. When
they got to the ship they found the crew waiting by the water side, and
Telemachus said, “Now my men, help me to get the stores on board; they
are all put together in the cloister, and my mother does not know
anything about it, nor any of the maid servants except one.”

With these words he led the way and the others followed after. When
they had brought the things as he told them, Telemachus went on board,
Minerva going before him and taking her seat in the stern of the
vessel, while Telemachus sat beside her. Then the men loosed the
hawsers and took their places on the benches. Minerva sent them a fair
wind from the West,22 that whistled over the deep blue waves23 whereon
Telemachus told them to catch hold of the ropes and hoist sail, and
they did as he told them. They set the mast in its socket in the cross
plank, raised it, and made it fast with the forestays; then they
hoisted their white sails aloft with ropes of twisted ox hide. As the
sail bellied out with the wind, the ship flew through the deep blue
water, and the foam hissed against her bows as she sped onward. Then
they made all fast throughout the ship, filled the mixing bowls to the
brim, and made drink offerings to the immortal gods that are from
everlasting, but more particularly to the grey-eyed daughter of Jove.

Thus, then, the ship sped on her way through the watches of the night
from dark till dawn.




BOOK III


TELEMACHUS VISITS NESTOR AT PYLOS.


but as the sun was rising from the fair sea24 into the firmament of
heaven to shed light on mortals and immortals, they reached Pylos the
city of Neleus. Now the people of Pylos were gathered on the sea shore
to offer sacrifice of black bulls to Neptune lord of the Earthquake.
There were nine guilds with five hundred men in each, and there were
nine bulls to each guild. As they were eating the inward meats25 and
burning the thigh bones [on the embers] in the name of Neptune,
Telemachus and his crew arrived, furled their sails, brought their ship
to anchor, and went ashore.

Minerva led the way and Telemachus followed her. Presently she said,
“Telemachus, you must not be in the least shy or nervous; you have
taken this voyage to try and find out where your father is buried and
how he came by his end; so go straight up to Nestor that we may see
what he has got to tell us. Beg of him to speak the truth, and he will
tell no lies, for he is an excellent person.”

“But how, Mentor,” replied Telemachus, “dare I go up to Nestor, and how
am I to address him? I have never yet been used to holding long
conversations with people, and am ashamed to begin questioning one who
is so much older than myself.”

“Some things, Telemachus,” answered Minerva, “will be suggested to you
by your own instinct, and heaven will prompt you further; for I am
assured that the gods have been with you from the time of your birth
until now.”

She then went quickly on, and Telemachus followed in her steps till
they reached the place where the guilds of the Pylian people were
assembled. There they found Nestor sitting with his sons, while his
company round him were busy getting dinner ready, and putting pieces of
meat on to the spits26 while other pieces were cooking. When they saw
the strangers they crowded round them, took them by the hand and bade
them take their places. Nestor’s son Pisistratus at once offered his
hand to each of them, and seated them on some soft sheepskins that were
lying on the sands near his father and his brother Thrasymedes. Then he
gave them their portions of the inward meats and poured wine for them
into a golden cup, handing it to Minerva first, and saluting her at the
same time.

“Offer a prayer, sir,” said he, “to King Neptune, for it is his feast
that you are joining; when you have duly prayed and made your drink
offering, pass the cup to your friend that he may do so also. I doubt
not that he too lifts his hands in prayer, for man cannot live without
God in the world. Still he is younger than you are, and is much of an
age with myself, so I will give you the precedence.”

As he spoke he handed her the cup. Minerva thought it very right and
proper of him to have given it to herself first;27 she accordingly
began praying heartily to Neptune. “O thou,” she cried, “that
encirclest the earth, vouchsafe to grant the prayers of thy servants
that call upon thee. More especially we pray thee send down thy grace
on Nestor and on his sons; thereafter also make the rest of the Pylian
people some handsome return for the goodly hecatomb they are offering
you. Lastly, grant Telemachus and myself a happy issue, in respect of
the matter that has brought us in our ship to Pylos.”

When she had thus made an end of praying, she handed the cup to
Telemachus and he prayed likewise. By and by, when the outer meats were
roasted and had been taken off the spits, the carvers gave every man
his portion and they all made an excellent dinner. As soon as they had
had enough to eat and drink, Nestor, knight of Gerene, began to speak.

“Now,” said he, “that our guests have done their dinner, it will be
best to ask them who they are. Who, then, sir strangers, are you, and
from what port have you sailed? Are you traders? or do you sail the
seas as rovers with your hand against every man, and every man’s hand
against you?”

Telemachus answered boldly, for Minerva had given him courage to ask
about his father and get himself a good name.

“Nestor,” said he, “son of Neleus, honour to the Achaean name, you ask
whence we come, and I will tell you. We come from Ithaca under
Neritum,28 and the matter about which I would speak is of private not
public import. I seek news of my unhappy father Ulysses, who is said to
have sacked the town of Troy in company with yourself. We know what
fate befell each one of the other heroes who fought at Troy, but as
regards Ulysses heaven has hidden from us the knowledge even that he is
dead at all, for no one can certify us in what place he perished, nor
say whether he fell in battle on the mainland, or was lost at sea amid
the waves of Amphitrite. Therefore I am suppliant at your knees, if
haply you may be pleased to tell me of his melancholy end, whether you
saw it with your own eyes, or heard it from some other traveller, for
he was a man born to trouble. Do not soften things out of any pity for
me, but tell me in all plainness exactly what you saw. If my brave
father Ulysses ever did you loyal service, either by word or deed, when
you Achaeans were harassed among the Trojans, bear it in mind now as in
my favour and tell me truly all.”

“My friend,” answered Nestor, “you recall a time of much sorrow to my
mind, for the brave Achaeans suffered much both at sea, while
privateering under Achilles, and when fighting before the great city of
king Priam. Our best men all of them fell there—Ajax, Achilles,
Patroclus peer of gods in counsel, and my own dear son Antilochus, a
man singularly fleet of foot and in fight valiant. But we suffered much
more than this; what mortal tongue indeed could tell the whole story?
Though you were to stay here and question me for five years, or even
six, I could not tell you all that the Achaeans suffered, and you would
turn homeward weary of my tale before it ended. Nine long years did we
try every kind of stratagem, but the hand of heaven was against us;
during all this time there was no one who could compare with your
father in subtlety—if indeed you are his son—I can hardly believe my
eyes—and you talk just like him too—no one would say that people of
such different ages could speak so much alike. He and I never had any
kind of difference from first to last neither in camp nor council, but
in singleness of heart and purpose we advised the Argives how all might
be ordered for the best.

“When, however, we had sacked the city of Priam, and were setting sail
in our ships as heaven had dispersed us, then Jove saw fit to vex the
Argives on their homeward voyage; for they had not all been either wise
or understanding, and hence many came to a bad end through the
displeasure of Jove’s daughter Minerva, who brought about a quarrel
between the two sons of Atreus.

“The sons of Atreus called a meeting which was not as it should be, for
it was sunset and the Achaeans were heavy with wine. When they
explained why they had called the people together, it seemed that
Menelaus was for sailing homeward at once, and this displeased
Agamemnon, who thought that we should wait till we had offered
hecatombs to appease the anger of Minerva. Fool that he was, he might
have known that he would not prevail with her, for when the gods have
made up their minds they do not change them lightly. So the two stood
bandying hard words, whereon the Achaeans sprang to their feet with a
cry that rent the air, and were of two minds as to what they should do.

“That night we rested and nursed our anger, for Jove was hatching
mischief against us. But in the morning some of us drew our ships into
the water and put our goods with our women on board, while the rest,
about half in number, stayed behind with Agamemnon. We—the other
half—embarked and sailed; and the ships went well, for heaven had
smoothed the sea. When we reached Tenedos we offered sacrifices to the
gods, for we were longing to get home; cruel Jove, however, did not yet
mean that we should do so, and raised a second quarrel in the course of
which some among us turned their ships back again, and sailed away
under Ulysses to make their peace with Agamemnon; but I, and all the
ships that were with me pressed forward, for I saw that mischief was
brewing. The son of Tydeus went on also with me, and his crews with
him. Later on Menelaus joined us at Lesbos, and found us making up our
minds about our course—for we did not know whether to go outside Chios
by the island of Psyra, keeping this to our left, or inside Chios, over
against the stormy headland of Mimas. So we asked heaven for a sign,
and were shown one to the effect that we should be soonest out of
danger if we headed our ships across the open sea to Euboea. This we
therefore did, and a fair wind sprang up which gave us a quick passage
during the night to Geraestus,29 where we offered many sacrifices to
Neptune for having helped us so far on our way. Four days later Diomed
and his men stationed their ships in Argos, but I held on for Pylos,
and the wind never fell light from the day when heaven first made it
fair for me.

“Therefore, my dear young friend, I returned without hearing anything
about the others. I know neither who got home safely nor who were lost
but, as in duty bound, I will give you without reserve the reports that
have reached me since I have been here in my own house. They say the
Myrmidons returned home safely under Achilles’ son Neoptolemus; so also
did the valiant son of Poias, Philoctetes. Idomeneus, again, lost no
men at sea, and all his followers who escaped death in the field got
safe home with him to Crete. No matter how far out of the world you
live, you will have heard of Agamemnon and the bad end he came to at
the hands of Aegisthus—and a fearful reckoning did Aegisthus presently
pay. See what a good thing it is for a man to leave a son behind him to
do as Orestes did, who killed false Aegisthus the murderer of his noble
father. You too, then—for you are a tall smart-looking fellow—show your
mettle and make yourself a name in story.”

“Nestor son of Neleus,” answered Telemachus, “honour to the Achaean
name, the Achaeans applaud Orestes and his name will live through all
time for he has avenged his father nobly. Would that heaven might grant
me to do like vengeance on the insolence of the wicked suitors, who are
ill treating me and plotting my ruin; but the gods have no such
happiness in store for me and for my father, so we must bear it as best
we may.”

“My friend,” said Nestor, “now that you remind me, I remember to have
heard that your mother has many suitors, who are ill disposed towards
you and are making havoc of your estate. Do you submit to this tamely,
or are public feeling and the voice of heaven against you? Who knows
but what Ulysses may come back after all, and pay these scoundrels in
full, either single-handed or with a force of Achaeans behind him? If
Minerva were to take as great a liking to you as she did to Ulysses
when we were fighting before Troy (for I never yet saw the gods so
openly fond of any one as Minerva then was of your father), if she
would take as good care of you as she did of him, these wooers would
soon some of them forget their wooing.”

Telemachus answered, “I can expect nothing of the kind; it would be far
too much to hope for. I dare not let myself think of it. Even though
the gods themselves willed it no such good fortune could befall me.”

On this Minerva said, “Telemachus, what are you talking about? Heaven
has a long arm if it is minded to save a man; and if it were me, I
should not care how much I suffered before getting home, provided I
could be safe when I was once there. I would rather this, than get home
quickly, and then be killed in my own house as Agamemnon was by the
treachery of Aegisthus and his wife. Still, death is certain, and when
a man’s hour is come, not even the gods can save him, no matter how
fond they are of him.”

“Mentor,” answered Telemachus, “do not let us talk about it any more.
There is no chance of my father’s ever coming back; the gods have long
since counselled his destruction. There is something else, however,
about which I should like to ask Nestor, for he knows much more than
any one else does. They say he has reigned for three generations so
that it is like talking to an immortal. Tell me, therefore, Nestor, and
tell me true; how did Agamemnon come to die in that way? What was
Menelaus doing? And how came false Aegisthus to kill so far better a
man than himself? Was Menelaus away from Achaean Argos, voyaging
elsewhither among mankind, that Aegisthus took heart and killed
Agamemnon?”

“I will tell you truly,” answered Nestor, “and indeed you have yourself
divined how it all happened. If Menelaus when he got back from Troy had
found Aegisthus still alive in his house, there would have been no
barrow heaped up for him, not even when he was dead, but he would have
been thrown outside the city to dogs and vultures, and not a woman
would have mourned him, for he had done a deed of great wickedness; but
we were over there, fighting hard at Troy, and Aegisthus, who was
taking his ease quietly in the heart of Argos, cajoled Agamemnon’s wife
Clytemnestra with incessant flattery.

“At first she would have nothing to do with his wicked scheme, for she
was of a good natural disposition;30 moreover there was a bard with
her, to whom Agamemnon had given strict orders on setting out for Troy,
that he was to keep guard over his wife; but when heaven had counselled
her destruction, Aegisthus carried this bard off to a desert island and
left him there for crows and seagulls to batten upon—after which she
went willingly enough to the house of Aegisthus. Then he offered many
burnt sacrifices to the gods, and decorated many temples with
tapestries and gilding, for he had succeeded far beyond his
expectations.

“Meanwhile Menelaus and I were on our way home from Troy, on good terms
with one another. When we got to Sunium, which is the point of Athens,
Apollo with his painless shafts killed Phrontis the steersman of
Menelaus’ ship (and never man knew better how to handle a vessel in
rough weather) so that he died then and there with the helm in his
hand, and Menelaus, though very anxious to press forward, had to wait
in order to bury his comrade and give him his due funeral rites.
Presently, when he too could put to sea again, and had sailed on as far
as the Malean heads, Jove counselled evil against him and made it blow
hard till the waves ran mountains high. Here he divided his fleet and
took the one half towards Crete where the Cydonians dwell round about
the waters of the river Iardanus. There is a high headland hereabouts
stretching out into the sea from a place called Gortyn, and all along
this part of the coast as far as Phaestus the sea runs high when there
is a south wind blowing, but after Phaestus the coast is more
protected, for a small headland can make a great shelter. Here this
part of the fleet was driven on to the rocks and wrecked; but the crews
just managed to save themselves. As for the other five ships, they were
taken by winds and seas to Egypt, where Menelaus gathered much gold and
substance among people of an alien speech. Meanwhile Aegisthus here at
home plotted his evil deed. For seven years after he had killed
Agamemnon he ruled in Mycene, and the people were obedient under him,
but in the eighth year Orestes came back from Athens to be his bane,
and killed the murderer of his father. Then he celebrated the funeral
rites of his mother and of false Aegisthus by a banquet to the people
of Argos, and on that very day Menelaus came home,31 with as much
treasure as his ships could carry.

“Take my advice then, and do not go travelling about for long so far
from home, nor leave your property with such dangerous people in your
house; they will eat up everything you have among them, and you will
have been on a fool’s errand. Still, I should advise you by all means
to go and visit Menelaus, who has lately come off a voyage among such
distant peoples as no man could ever hope to get back from, when the
winds had once carried him so far out of his reckoning; even birds
cannot fly the distance in a twelve-month, so vast and terrible are the
seas that they must cross. Go to him, therefore, by sea, and take your
own men with you; or if you would rather travel by land you can have a
chariot, you can have horses, and here are my sons who can escort you
to Lacedaemon where Menelaus lives. Beg of him to speak the truth, and
he will tell you no lies, for he is an excellent person.”

As he spoke the sun set and it came on dark, whereon Minerva said,
“Sir, all that you have said is well; now, however, order the tongues
of the victims to be cut, and mix wine that we may make drink-offerings
to Neptune, and the other immortals, and then go to bed, for it is bed
time. People should go away early and not keep late hours at a
religious festival.”

Thus spoke the daughter of Jove, and they obeyed her saying. Men
servants poured water over the hands of the guests, while pages filled
the mixing-bowls with wine and water, and handed it round after giving
every man his drink offering; then they threw the tongues of the
victims into the fire, and stood up to make their drink offerings. When
they had made their offerings and had drunk each as much as he was
minded, Minerva and Telemachus were for going on board their ship, but
Nestor caught them up at once and stayed them.

“Heaven and the immortal gods,” he exclaimed, “forbid that you should
leave my house to go on board of a ship. Do you think I am so poor and
short of clothes, or that I have so few cloaks and as to be unable to
find comfortable beds both for myself and for my guests? Let me tell
you I have store both of rugs and cloaks, and shall not permit the son
of my old friend Ulysses to camp down on the deck of a ship—not while I
live—nor yet will my sons after me, but they will keep open house as I
have done.”

Then Minerva answered, “Sir, you have spoken well, and it will be much
better that Telemachus should do as you have said; he, therefore, shall
return with you and sleep at your house, but I must go back to give
orders to my crew, and keep them in good heart. I am the only older
person among them; the rest are all young men of Telemachus’ own age,
who have taken this voyage out of friendship; so I must return to the
ship and sleep there. Moreover to-morrow I must go to the Cauconians
where I have a large sum of money long owing to me. As for Telemachus,
now that he is your guest, send him to Lacedaemon in a chariot, and let
one of your sons go with him. Be pleased to also provide him with your
best and fleetest horses.”

When she had thus spoken, she flew away in the form of an eagle, and
all marvelled as they beheld it. Nestor was astonished, and took
Telemachus by the hand. “My friend,” said he, “I see that you are going
to be a great hero some day, since the gods wait upon you thus while
you are still so young. This can have been none other of those who
dwell in heaven than Jove’s redoubtable daughter, the Trito-born, who
shewed such favour towards your brave father among the Argives. Holy
queen,” he continued, “vouchsafe to send down thy grace upon myself, my
good wife, and my children. In return, I will offer you in sacrifice a
broad-browed heifer of a year old, unbroken, and never yet brought by
man under the yoke. I will gild her horns, and will offer her up to you
in sacrifice.”

Thus did he pray, and Minerva heard his prayer. He then led the way to
his own house, followed by his sons and sons in law. When they had got
there and had taken their places on the benches and seats, he mixed
them a bowl of sweet wine that was eleven years old when the
housekeeper took the lid off the jar that held it. As he mixed the
wine, he prayed much and made drink offerings to Minerva, daughter of
Aegis-bearing Jove. Then, when they had made their drink offerings and
had drunk each as much as he was minded, the others went home to bed
each in his own abode; but Nestor put Telemachus to sleep in the room
that was over the gateway along with Pisistratus, who was the only
unmarried son now left him. As for himself, he slept in an inner room
of the house, with the queen his wife by his side.

Now when the child of morning rosy-fingered Dawn appeared, Nestor left
his couch and took his seat on the benches of white and polished marble
that stood in front of his house. Here aforetime sat Neleus, peer of
gods in counsel, but he was now dead, and had gone to the house of
Hades; so Nestor sat in his seat sceptre in hand, as guardian of the
public weal. His sons as they left their rooms gathered round him,
Echephron, Stratius, Perseus, Aretus, and Thrasymedes; the sixth son
was Pisistratus, and when Telemachus joined them they made him sit with
them. Nestor then addressed them.

“My sons,” said he, “make haste to do as I shall bid you. I wish first
and foremost to propitiate the great goddess Minerva, who manifested
herself visibly to me during yesterday’s festivities. Go, then, one or
other of you to the plain, tell the stockman to look me out a heifer,
and come on here with it at once. Another must go to Telemachus’ ship,
and invite all the crew, leaving two men only in charge of the vessel.
Some one else will run and fetch Laerceus the goldsmith to gild the
horns of the heifer. The rest, stay all of you where you are; tell the
maids in the house to prepare an excellent dinner, and to fetch seats,
and logs of wood for a burnt offering. Tell them also to bring me some
clear spring water.”

On this they hurried off on their several errands. The heifer was
brought in from the plain, and Telemachus’s crew came from the ship;
the goldsmith brought the anvil, hammer, and tongs, with which he
worked his gold, and Minerva herself came to accept the sacrifice.
Nestor gave out the gold, and the smith gilded the horns of the heifer
that the goddess might have pleasure in their beauty. Then Stratius and
Echephron brought her in by the horns; Aretus fetched water from the
house in a ewer that had a flower pattern on it, and in his other hand
he held a basket of barley meal; sturdy Thrasymedes stood by with a
sharp axe, ready to strike the heifer, while Perseus held a bucket.
Then Nestor began with washing his hands and sprinkling the barley
meal, and he offered many a prayer to Minerva as he threw a lock from
the heifer’s head upon the fire.

When they had done praying and sprinkling the barley meal32 Thrasymedes
dealt his blow, and brought the heifer down with a stroke that cut
through the tendons at the base of her neck, whereon the daughters and
daughters in law of Nestor, and his venerable wife Eurydice (she was
eldest daughter to Clymenus) screamed with delight. Then they lifted
the heifer’s head from off the ground, and Pisistratus cut her throat.
When she had done bleeding and was quite dead, they cut her up. They
cut out the thigh bones all in due course, wrapped them round in two
layers of fat, and set some pieces of raw meat on the top of them; then
Nestor laid them upon the wood fire and poured wine over them, while
the young men stood near him with five-pronged spits in their hands.
When the thighs were burned and they had tasted the inward meats, they
cut the rest of the meat up small, put the pieces on the spits and
toasted them over the fire.

Meanwhile lovely Polycaste, Nestor’s youngest daughter, washed
Telemachus. When she had washed him and anointed him with oil, she
brought him a fair mantle and shirt,33 and he looked like a god as he
came from the bath and took his seat by the side of Nestor. When the
outer meats were done they drew them off the spits and sat down to
dinner where they were waited upon by some worthy henchmen, who kept
pouring them out their wine in cups of gold. As soon as they had had
enough to eat and drink Nestor said, “Sons, put Telemachus’s horses to
the chariot that he may start at once.”

Thus did he speak, and they did even as he had said, and yoked the
fleet horses to the chariot. The housekeeper packed them up a provision
of bread, wine, and sweet meats fit for the sons of princes. Then
Telemachus got into the chariot, while Pisistratus gathered up the
reins and took his seat beside him. He lashed the horses on and they
flew forward nothing loth into the open country, leaving the high
citadel of Pylos behind them. All that day did they travel, swaying the
yoke upon their necks till the sun went down and darkness was over all
the land. Then they reached Pherae where Diocles lived, who was son to
Ortilochus and grandson to Alpheus. Here they passed the night and
Diocles entertained them hospitably. When the child of morning,
rosy-fingered Dawn, appeared, they again yoked their horses and drove
out through the gateway under the echoing gatehouse.34 Pisistratus
lashed the horses on and they flew forward nothing loth; presently they
came to the corn lands of the open country, and in the course of time
completed their journey, so well did their steeds take them.35

Now when the sun had set and darkness was over the land.

'''
#clean the data
corpus = corpus.lower()
punc = '''±¬¤¸£×¥¿*¶¼¦¹¯§¾´ª½¢¡®…³=²º­¨0123456789!→°()-[]{};:'"«»\,+<>./?@#$%^&*_~©'''
corpus = corpus.lower()
for x in corpus:
    if x in punc:
        corpus = corpus.replace(x,'')
corpus = corpus.replace('\n', ' ')
tokens = corpus.split(' ')
sentences = corpus.split('.')
tokens.remove('')
vocabulary = set(tokens)

t_cocc =[]
for sentence in sentences:
    for word1 in sentence.split(' '):
        for word2 in sentence.split(' '):
            if word1 != word2:
                t_cocc.append((word1,word2))

hist = nltk.FreqDist(t_cocc).most_common(len(t_cocc))
co_occ_mat = np.zeros((len(vocabulary), len(vocabulary)))
dic_ind = {w:i for i,w in enumerate(vocabulary)}

for element in hist:
    current = element[0][1]
    previous = element[0][0]
    freq = element[1]
    index_c = dic_ind[current]
    index_p = dic_ind[previous]
    co_occ_mat[index_c][index_p] = freq

word_2_vec = {}
for word in vocabulary:
    word_2_vec[word] = co_occ_mat[dic_ind[word]]

print(co_occ_mat)
u,s,v = svd(co_occ_mat)
suma = 0
ori = 0
for i in range(len(s)):
    ori = ori +  pow(s[i],2)
r = 0
k = 0
original = s
print(u.shape)
while r <.97:
    s = original[0:k]
    for i in range(len(s)):
        suma = suma +  pow(s[i],2)
    print(suma)
    print(ori)
    r = suma/ori
    print(r)
    print(k)
    k = k +1
    suma = 0
u = u[0:, 0:k+1]
f = open('mapping.txt', 'w', encoding='utf-8')
i = 0
for el in vocabulary:
    f.write(el + str(u[i]) + '\n')
    i = i + 1
f.close()
