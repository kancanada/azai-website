Q = [
# (group, quote, cite, note)
("m", "In the morning when thou risest unwillingly, let this thought be present,—I am rising to the work of a human being.", "Marcus Aurelius, <em>Meditations</em> 5.1, tr. George Long", "Written by a Roman emperor who, by his own account, sometimes didn't want to get out of bed. The reframe is simple: the day's work isn't an imposition, it's what you're for."),
("m", "Begin the morning by saying to thyself, I shall meet with the busybody, the ungrateful, arrogant, deceitful, envious, unsocial.", "Marcus Aurelius, <em>Meditations</em> 2.1, tr. George Long", "This sounds cynical, but read on in the passage and it's the opposite: he expects difficult people so that he won't be thrown by them, and reminds himself that they're his kin, not his enemies."),
("m", "If thou art pained by any external thing, it is not this thing that disturbs thee, but thy own judgment about it.", "Marcus Aurelius, <em>Meditations</em> 8.47, tr. George Long", "The core Stoic move. You can't always change what happened, but you can examine the story you're telling about it."),
("m", "The universe is transformation: life is opinion.", "Marcus Aurelius, <em>Meditations</em> 4.3, tr. George Long", "Seven words that cover two of Marcus's favourite themes: everything changes, and much of how we experience it depends on our view of it."),
("m", "…it is in thy power whenever thou shalt choose to retire into thyself.", "Marcus Aurelius, <em>Meditations</em> 4.3, tr. George Long", "From a passage about how people long for retreats in the country or by the sea. His point: you can take a short retreat in your own mind at any moment, which is about as good a description of a one-minute morning practice as you'll find."),
("m", "Be like the promontory against which the waves continually break, but it stands firm and tames the fury of the water around it.", "Marcus Aurelius, <em>Meditations</em> 4.49, tr. George Long", "An image to borrow on a hard day: not fighting the waves, just not being moved by them."),
("m", "Do not act as if thou wert going to live ten thousand years. Death hangs over thee. While thou livest, while it is in thy power, be good.", "Marcus Aurelius, <em>Meditations</em> 4.17, tr. George Long", "The Stoics used the thought of death to sharpen attention, not to frighten. The instruction that follows is the important part: be good, now."),
("m", "Think not so much of what thou hast not as of what thou hast", "Marcus Aurelius, <em>Meditations</em> 7.27, tr. George Long", "Marcus goes on to add a caution: enjoy what you have without becoming so attached that losing it would undo you."),
("m", "Look within. Within is the fountain of good, and it will ever bubble up, if thou wilt ever dig.", "Marcus Aurelius, <em>Meditations</em> 7.59, tr. George Long", "Note the condition at the end. The good is there, but you have to keep digging."),
("m", "No longer talk at all about the kind of man that a good man ought to be, but be such.", "Marcus Aurelius, <em>Meditations</em> 10.16, tr. George Long", "Probably the most quoted line in the Meditations, usually in a shorter modern translation. It's a good check on any reflection habit, tarot included: reflection is only useful if it turns into action."),
("m", "If it is not right, do not do it: if it is not true, do not say it.", "Marcus Aurelius, <em>Meditations</em> 12.17, tr. George Long", "As close to a complete ethics in one sentence as you'll find."),
("m", "The best way of avenging thyself is not to become like [the wrong-doer].", "Marcus Aurelius, <em>Meditations</em> 6.6, tr. George Long", "The brackets are Long's: the Greek is shorter still. Often paraphrased as “the best revenge is not to be like your enemy”."),
("m", "Remember that to change thy opinion and to follow him who corrects thy error is as consistent with freedom as it is to persist in thy error.", "Marcus Aurelius, <em>Meditations</em> 8.16, tr. George Long", "Changing your mind isn't defeat. An emperor, of all people, reminding himself to take correction."),
("e", "Of things some are in our power, and others are not.", "Epictetus, <em>Encheiridion</em> 1, tr. George Long", "The first line of Epictetus's handbook and the foundation of Stoic practice. Our opinions, desires and actions are up to us; our body, property and reputation, in the end, are not."),
("e", "Men are disturbed not by the things which happen, but by the opinions about the things", "Epictetus, <em>Encheiridion</em> 5, tr. George Long", "The same insight as Marcus's 8.47; Marcus had read Epictetus closely."),
("e", "Seek not that the things which happen should happen as you wish; but wish the things which happen to be as they are, and you will have a tranquil flow of life.", "Epictetus, <em>Encheiridion</em> 8, tr. George Long", "Not resignation, but a refusal to waste energy wishing the past were different."),
("e", "Every habit and faculty is maintained and increased by the corresponding actions: the habit of walking by walking, the habit of running by running.", "Epictetus, <em>Discourses</em> 2.18, tr. George Long", "He continues: if you would be a good reader, read. The case for small daily practice, two thousand years before habit research."),
("e", "If you would improve, submit to be considered without sense and foolish with respect to externals.", "Epictetus, <em>Encheiridion</em> 13, tr. George Long", "Progress sometimes means caring less about how you look to other people."),
("s", "Nothing, Lucilius, is ours, except time.", "Seneca, <em>Moral Letters to Lucilius</em> 1.3, tr. Richard M. Gummere", "Seneca's first letter is about wasted time. He goes on to call time the one loan that even a grateful person can't repay."),
("s", "Lay hold of to-day's task, and you will not need to depend so much upon to-morrow's. While we are postponing, life speeds by.", "Seneca, <em>Moral Letters to Lucilius</em> 1.2, tr. Richard M. Gummere", "Practical advice for anyone with a to-do list."),
("s", "There are more things, Lucilius, likely to frighten us than there are to crush us; we suffer more often in imagination than in reality.", "Seneca, <em>Moral Letters to Lucilius</em> 13.4, tr. Richard M. Gummere", "Worth rereading the night before anything you're dreading."),
("s", "…after you have run over many thoughts, select one to be thoroughly digested that day.", "Seneca, <em>Moral Letters to Lucilius</em> 2.4, tr. Richard M. Gummere", "Seneca's own recommendation for daily reading: not many ideas skimmed, but one idea chewed over. It's the method this whole guide is built on."),
]

def block(g):
    return "".join(f'<blockquote>“{q}”</blockquote><p class="cite">{c}</p><p>{n}</p>' for gg, q, c, n in Q if gg == g)

A = dict(
order=7,
slug="stoic-quotes-daily-reflection",
title="Stoic Quotes for Daily Reflection, with Sources | Daily Oracle",
h1="Stoic quotes for daily reflection, with sources",
desc="22 Stoic quotes from Marcus Aurelius, Epictetus and Seneca, quoted word for word from public-domain translations, with exact references and how to use them.",
answer="The three great Stoic writers, Marcus Aurelius, Epictetus and Seneca, all wrote short, practical lines meant to be reread daily. Below are 22 of the best, quoted word for word from public-domain translations (George Long for Marcus and Epictetus, Richard M. Gummere for Seneca), each with its book and section so you can check it. Seneca's own advice is the best way to use them: read widely, then pick one thought and digest it that day.",
disclose="We make Daily Oracle, a free Android app (with ads) that shows one Stoic quote a day from Marcus Aurelius or Epictetus in George Long's translations; we mention it near the end. The app doesn't include Seneca.",
body="""<p>Stoic quotes are everywhere online, and a surprising number of them are misattributed, paraphrased beyond recognition, or taken from modern translations without credit. This page sticks to lines we've checked against the source texts. Every quote below is copied from a public-domain translation, with the book and section number so you can find it yourself. After each one there's a short note on what it means in context and how you might use it.</p>

<h2>The three Stoic writers, briefly</h2>
<p><b>Marcus Aurelius</b> (121–180 CE) was Roman emperor from 161. His <em>Meditations</em> are private notes to himself, written in Greek, many of them during military campaigns. He never meant them to be published, which is why they read like someone talking himself into being a better person, because that's what they are.</p>
<p><b>Epictetus</b> (about 50–135 CE) was born into slavery, later freed, and taught philosophy in Rome and then Nicopolis in Greece. He wrote nothing himself. His student Arrian recorded his lectures as the <em>Discourses</em> and summarised his teaching in a short handbook, the <em>Encheiridion</em> (often spelled <em>Enchiridion</em>).</p>
<p><b>Seneca</b> (about 4 BCE–65 CE) was a Roman statesman, playwright and adviser to the emperor Nero. His <em>Moral Letters to Lucilius</em>, 124 letters to a younger friend, are the warmest and most conversational Stoic writing we have.</p>

<h2>About the translations</h2>
<p>We quote George Long's 19th-century translations of Marcus Aurelius and Epictetus, and Richard Mott Gummere's translation of Seneca's letters, published in the Loeb Classical Library from 1917. All are in the public domain in the United States, which means they can be quoted freely and checked by anyone on Project Gutenberg or Wikisource.</p>
<p>Long's English is old-fashioned, with “thou” and “thy”, and some popular modern translations read more smoothly. But many of the snappy versions you see on social media come from recent translations that are still under copyright, or are loose paraphrases that drift from what was written. If you share a Stoic quote, it's worth knowing which translation it's from.</p>

<h2>Marcus Aurelius, <em>Meditations</em></h2>
""" + block("m") + """

<h2>Epictetus, <em>Encheiridion</em> and <em>Discourses</em></h2>
""" + block("e") + """

<h2>Seneca, <em>Moral Letters to Lucilius</em></h2>
""" + block("s") + """

<h2>How to use a Stoic quote each day</h2>
<p>A quote you read and scroll past does nothing. A quote you carry around for a day can change how you handle it. Here's a simple method, in the spirit of Seneca's second letter:</p>
<ol>
<li><b>Read one quote in the morning.</b> Just one. Read it twice, slowly.</li>
<li><b>Put it in your own words.</b> Write a single line: “Don't argue about being good. Be good.” If you can't paraphrase it, you haven't understood it yet.</li>
<li><b>Find one place it applies today.</b> A meeting, a commute, a conversation you're dreading. Name it.</li>
<li><b>Check back in the evening.</b> Did you remember the quote when it mattered? What happened?</li>
</ol>
<p>It also pairs well with a daily tarot card. The card gives you an image, the quote gives you a principle, and the two often rub against each other in useful ways: the Tower next to “we suffer more often in imagination than in reality”, or the Chariot next to “the habit of walking by walking”. Our guide to <a href="one-minute-morning-ritual.html">a one-minute morning ritual</a> puts the pieces together.</p>

<h2>A note on misattributed Stoic quotes</h2>
<p>A few habits help you avoid sharing a fake one:</p>
<ul>
<li><b>Look for a reference.</b> A real quote can be located: book and section for Marcus, chapter for Epictetus, letter number for Seneca. If a quote has no reference, be suspicious.</li>
<li><b>Search the source text.</b> Long's and Gummere's translations are free online. Search a distinctive word from the quote.</li>
<li><b>Watch for modern vocabulary.</b> Words like “mindset”, “energy” or “vibe” didn't come from a Roman.</li>
<li><b>Paraphrase is fine, if labelled.</b> “As Marcus Aurelius put it, roughly…” is honest. Putting your own wording in quotation marks isn't.</li>
</ul>

<h2>Stoicism and daily reflection</h2>
<p>The Stoics didn't think philosophy was something you studied once; they thought it was something you practised every day, like exercise. Marcus's notebook is the proof: a powerful man, returning again and again to the same few ideas because he kept forgetting them. That's encouraging. A daily quote isn't about finding a new insight every morning. It's about being reminded of a handful of true things often enough that they're there when you need them.</p>

<h2>A Stoic line every day in Daily Oracle</h2>
<p>Daily Oracle, our Android app, includes 365 Stoic quotes, a different one for each day of the year, from Marcus Aurelius's <em>Meditations</em> and Epictetus's <em>Encheiridion</em> and <em>Discourses</em>, in George Long's translations, quoted word for word with their references. Each day's quote sits alongside a tarot card from the 1909 Rider-Waite-Smith deck with a reflection and a journaling question, one small action, and tonight's moon phase and moon sign. It's free with ads, works offline and needs no account.</p>
{{CTA}}
""",
faq=[
("What is the most famous Stoic quote?", "Strong candidates are Epictetus's “Men are disturbed not by the things which happen, but by the opinions about the things” (Encheiridion 5) and Marcus Aurelius's “No longer talk at all about the kind of man that a good man ought to be, but be such” (Meditations 10.16), both in George Long's translation."),
("Which translation of Marcus Aurelius should I read?", "George Long's 19th-century translation is in the public domain and free online, but its English is old-fashioned. Several modern translations read more easily; they're under copyright. Many people read a modern one and check lines against Long."),
("Did Seneca say “we suffer more in imagination than in reality”?", "Yes. In Gummere's translation of Moral Letters to Lucilius, letter 13, section 4: “we suffer more often in imagination than in reality.”"),
("How do I use Stoic quotes for daily reflection?", "Read one quote in the morning, rewrite it in your own words, name one situation today where it applies, and check back in the evening. Seneca recommended choosing one thought to digest each day."),
("Are Stoic quotes public domain?", "The original Greek and Latin texts are. Translations have their own copyright: George Long's translations of Marcus Aurelius and Epictetus, and Gummere's translation of Seneca from 1917 onwards, are public domain in the US; many modern translations aren't."),
],
sources=[
("Marcus Aurelius, Thoughts (Meditations), tr. George Long, Project Gutenberg", "https://www.gutenberg.org/ebooks/15877"),
("Epictetus, A Selection from the Discourses with the Encheiridion, tr. George Long, Project Gutenberg", "https://www.gutenberg.org/ebooks/10661"),
("Seneca, Moral Letters to Lucilius, tr. Richard M. Gummere, Letter 1 (Wikisource)", "https://en.wikisource.org/wiki/Moral_letters_to_Lucilius/Letter_1"),
("Seneca, Moral Letters to Lucilius, Letter 2 (Wikisource)", "https://en.wikisource.org/wiki/Moral_letters_to_Lucilius/Letter_2"),
("Seneca, Moral Letters to Lucilius, Letter 13 (Wikisource)", "https://en.wikisource.org/wiki/Moral_letters_to_Lucilius/Letter_13"),
("Cornell University Library: copyright term and the public domain in the United States", "https://guides.library.cornell.edu/copyright/publicdomain"),
],
srcnote="Every quote was checked word for word against the linked texts on 15 November 2026. Section numbers follow those editions.",
)
