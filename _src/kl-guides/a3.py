from base import GUIDES
from a1 import DISC_STD, S_PRT, S_PEN, S_FCAC, S_KL
from a2 import S_YNAB_MANUAL, S_YNAB_LINK, S_YNAB_PRICE, S_GB, S_GB_PLAY, S_CASHEW, S_CASHEW_GH

S_MM = ("Money Manager Expense & Budget on Google Play", "https://play.google.com/store/apps/details?id=com.realbyteapps.moneymanagerfree")
S_ACTUAL = ("Actual Budget (open-source, local-first budgeting)", "https://actualbudget.org/")
S_HALIL = ("Kakeibo: Budget Planner (Halil Apps) on Google Play", "https://play.google.com/store/apps/details?id=com.halil.kakeibo")
S_PALP = ("Kakeibo: Budget & Expense Log (Pablo Muñoz García) on Google Play", "https://play.google.com/store/apps/details?id=dev.palpfiction.kakeibo")
S_RELLOW = ("Kakebo: Track Expense & Budget (RellowTeam) on Google Play", "https://play.google.com/store/apps/details?id=com.rellowteam.kakebo2")
S_PLAY_DS = ("Google Play Help: the Data safety section", "https://support.google.com/googleplay/answer/11416267")

# ---------------------------------------------------------------- 6
GUIDES.append(dict(
slug="no-spend-challenge",
h1="How to do a no-spend month (and learn something from it)",
title="No-Spend Month Challenge: Rules, Plan and What to Track | Kakeibo Ledger",
desc="How to run a no-spend month or week: setting rules that fit your life, preparing, handling social plans, what to track, and what to do with the money afterwards.",
answer=("A no-spend month means buying only what you&#x27;ve agreed in advance is essential (usually bills, groceries, transport and medicine) and nothing else for a set period. "
        "It works best with written rules made before you start, a short list of allowed exceptions, a plan for social invitations, and a daily record of what you did spend. "
        "Start with a weekend or a week if a month feels like too much, and decide in advance where the money you don&#x27;t spend will go."),
disclose=DISC_STD,
body="""<p>A no-spend challenge is a short, deliberate pause on optional spending. It&#x27;s popular because it&#x27;s simple and because a few weeks without casual purchases shows you, very clearly, which of them you actually miss. Done badly, it&#x27;s a month of white-knuckling followed by a splurge. Done well, it resets habits and frees up real money.</p>
<p>This guide covers how to set it up, how to get through it, and how to use what you learn. It pairs naturally with kakeibo, the Japanese ledger method, because both are about noticing spending rather than automating it.</p>

<h2>What &ldquo;no spend&rdquo; actually means</h2>
<p>Nobody stops spending entirely. Rent is still due and you still need to eat. A no-spend month means you&#x27;ve drawn a line in advance between essentials, which you keep paying for, and everything else, which you pause. The line is personal. A sensible default:</p>
<div class="table"><table>
<tr><th>Usually allowed</th><th>Usually paused</th></tr>
<tr><td>Rent or mortgage, utilities, insurance, phone and internet</td><td>Restaurants, takeaway, delivery and coffee out</td></tr>
<tr><td>Groceries from a list</td><td>Clothes, shoes and accessories</td></tr>
<tr><td>Fuel, transit, parking for work</td><td>Gadgets, games, apps and in-app purchases</td></tr>
<tr><td>Prescriptions and medical care</td><td>Home decor and &ldquo;organizing&rdquo; purchases</td></tr>
<tr><td>Debt payments and savings transfers</td><td>New subscriptions and upgrades</td></tr>
<tr><td>Genuine emergencies and repairs</td><td>Impulse buys online, including &ldquo;it was on sale&rdquo;</td></tr>
</table></div>
<p>In kakeibo terms: needs and unexpected stay open; wants go to zero; culture is your call. Many people keep a small culture allowance (a library card is free, but a course you&#x27;ve already started shouldn&#x27;t be abandoned).</p>

<h2>Choose your length</h2>
<ul>
<li><b>A no-spend weekend</b> is a good first test. Plan free activities, eat what&#x27;s in the fridge, and see how often you reach for your card out of habit.</li>
<li><b>A no-spend week</b> covers a full work cycle, including the weekday lunches and after-work treats that add up fastest.</li>
<li><b>A no-spend month</b> is long enough to change habits and to make a noticeable difference to savings, and long enough that you need rules for birthdays and plans with friends.</li>
</ul>
<p>Pick a month without a big holiday, wedding or trip in it. You&#x27;re trying to learn about ordinary months, and setting yourself up to fail teaches nothing.</p>

<h2>Write your rules before you start</h2>
<p>The single most useful step is putting your rules in writing. Vague intentions get renegotiated at the till; written rules don&#x27;t. A good rule sheet answers these:</p>
<ol>
<li><b>What&#x27;s allowed?</b> List the categories, not just &ldquo;essentials&rdquo;.</li>
<li><b>What&#x27;s the grocery limit?</b> A weekly amount stops groceries becoming a loophole for snacks and wine.</li>
<li><b>What about gifts?</b> Decide now whether you&#x27;ll buy them, make them or postpone them.</li>
<li><b>What about social plans?</b> For example: &ldquo;I&#x27;ll suggest free plans first; if I go out, one drink, paid from a $40 social allowance for the month.&rdquo;</li>
<li><b>What if something breaks?</b> Real repairs and replacements are allowed. Upgrades aren&#x27;t.</li>
<li><b>What happens if I slip?</b> Write it down, note why, and carry on. One slip doesn&#x27;t end the month.</li>
</ol>
<p>Share the rules with anyone you live with. A no-spend month one person keeps and the other doesn&#x27;t know about tends to end on day four.</p>

<h2>Prepare in the week before</h2>
<ul>
<li><b>Check your calendar</b> for birthdays, renewals and events, and decide how you&#x27;ll handle each.</li>
<li><b>Make a meal plan</b> and shop for staples, but don&#x27;t stockpile. Buying a month of treats in advance just moves the spending.</li>
<li><b>Unsubscribe from shop emails</b> and remove saved cards from the shopping sites you use most. Friction helps.</li>
<li><b>Delete or log out of food delivery apps</b> for the month.</li>
<li><b>Make a free-things list:</b> library, parks, free museum days, hikes, a potluck instead of a restaurant, the films you already own.</li>
<li><b>Decide where the savings go.</b> Moving the money you expect to save into savings on day one makes it real, and removes the temptation to spend it on day 31.</li>
</ul>

<h2>Track every day, including what you didn&#x27;t buy</h2>
<p>Tracking is what turns a no-spend month from a test of willpower into something you learn from. Keep a daily record of:</p>
<ul>
<li><b>Everything you did spend</b>, with its category. Allowed spending still counts; it shows what your true essentials cost.</li>
<li><b>No-spend days</b>, marked with a tick. Seeing a run of them is motivating.</li>
<li><b>Urges</b>: what you wanted to buy, when, and why. &ldquo;Wednesday, 3pm, bored at work, wanted a coffee and pastry&rdquo; is gold for your month-end reflection.</li>
</ul>
<p>A paper ledger works well for this; our <a href="kakeibo-template.html">kakeibo template</a> has the columns, and you can use the &ldquo;what&rdquo; column for urges too. Our guide to <a href="track-expenses-by-hand.html">tracking expenses by hand</a> has tips for keeping it up.</p>

<h2>Handling the hard moments</h2>
<p><b>Friends want to go out.</b> Suggest an alternative that costs nothing or little: a walk, a meal at home, a free event. If you go out, use your social allowance and order before you&#x27;re hungry or tired. Most friends respect &ldquo;I&#x27;m doing a no-spend month&rdquo; more than you&#x27;d expect, and some will join in.</p>
<p><b>You see a sale.</b> Write it on a wish list with the date. If you still want it in 30 days, buy it then with a clear head. Most items on the list won&#x27;t survive the month.</p>
<p><b>You slip.</b> Record it honestly, note what triggered it, and carry on. A month with two slips is still a month with fifty fewer optional purchases than usual.</p>
<p><b>Week three drags.</b> This is when most people quit. Look at your no-spend day ticks and what you&#x27;ve saved so far. Plan one good free thing for that weekend.</p>

<h2>After the month: reflect before you spend</h2>
<p>The end of the month is the most important part, and the easiest to skip. Before you go back to normal, sit down for twenty minutes and answer:</p>
<ol>
<li>How much did I spend in total, and how does that compare with a normal month?</li>
<li>What did I miss most? (Those are probably worth budgeting for.)</li>
<li>What didn&#x27;t I miss at all? (Those are habits, not wants. Consider dropping them.)</li>
<li>When did the urges come? (Time of day, mood, place.)</li>
<li>What one change will I keep next month?</li>
</ol>
<p>That&#x27;s essentially the kakeibo month-end reflection, aimed at a no-spend month. Our <a href="monthly-budget-reflection-questions.html">monthly reflection guide</a> has more questions if you want to go deeper.</p>
<p>Then ease back in. A common mistake is the &ldquo;reward&rdquo; spree on day one of the next month, which can undo most of the savings. Plan one deliberate treat from the list of things you missed, and keep the rest of the new habits.</p>

<h2>Is a no-spend month right for you?</h2>
<p>It&#x27;s a good tool if you suspect small optional purchases are leaking money, or if you want to jump-start savings for a goal. It&#x27;s less useful if your budget problem is structural (high rent, debt payments, low income), because there may be little optional spending to cut. In that case a full budget and, if you&#x27;re in debt, a conversation with a non-profit credit counsellor will help more than a challenge.</p>
<p>It&#x27;s also not a good idea to pause essential spending like medication or necessary repairs to &ldquo;win&rdquo;. The aim is awareness, not deprivation.</p>

<h2>Doing it with Kakeibo Ledger</h2>
<p>Kakeibo Ledger, which we make, doesn&#x27;t have a special no-spend mode, but its plan works well for one. Set the wants share of your spending money to zero (and culture too, if you&#x27;re pausing it), keep needs and unexpected, and record every purchase as usual. The Sunday check-in shows your week against the plan, and at month end the reflection screen fills in the totals and asks what you&#x27;ll change. It doesn&#x27;t go online and has no ads, so it won&#x27;t tempt you with offers mid-challenge. If you want a calendar of no-spend days and streaks, the Halil Apps kakeibo app on Google Play lists that feature.</p>
""",
faqs=[
("What is allowed in a no-spend month?", "Usually bills, rent, groceries from a list, transport, medicine, debt payments and genuine emergencies. Optional spending such as eating out, shopping, gadgets and new subscriptions is paused. Write your own list before you start."),
("How much can you save with a no-spend month?", "It depends on how much optional spending you normally do. Add up last month's restaurants, takeaway, shopping and impulse buys; that is roughly the ceiling. Moving that amount to savings on day one helps you keep it."),
("Should I start with a no-spend week or month?", "If you have never tried it, start with a weekend or a week. A month changes habits more but needs rules for social plans, gifts and repairs."),
("What if I break my no-spend challenge?", "Record the purchase, note what triggered it, and continue. One slip doesn't cancel the month, and the trigger is useful information for your end-of-month reflection."),
("How does kakeibo help with a no-spend month?", "Kakeibo's four categories make the rules easy: keep needs and unexpected, set wants to zero, decide about culture. Writing every expense down and reflecting at month end turns the challenge into lasting changes."),
],
sources=[S_FCAC, S_PEN, S_HALIL, S_KL],
source_note="Checked on 15 November 2026. This guide is general information, not financial advice.",
))

# ---------------------------------------------------------------- 7
GUIDES.append(dict(
slug="budget-app-without-bank-linking",
h1="Budget apps that don't link to your bank (Android, 2026)",
title="Budget Apps That Don't Link to Your Bank: Private Android Options | Kakeibo Ledger",
desc="Budget apps that work without linking your bank account, compared for Android: what each costs, what its Data safety label says, where your data lives, and how to check.",
answer=("Several good budget apps work without a bank connection. On Android: Kakeibo Ledger (kakeibo method, no internet permission, free with a one-time Pro), Cashew (free, open source, data on your device), Goodbudget (envelopes; free plan with manual entry, data synced through its servers), Money Manager (detailed ledger, ads in the free version) and YNAB with unlinked accounts (subscription). "
        "The trade-off is the same for all of them: you enter spending yourself. To judge privacy, check the Data safety label, whether an account is required, and whether the app uses the internet at all."),
disclose=("We make Kakeibo Ledger, one of the apps compared here. We haven&#x27;t tested every app below; details come from each app&#x27;s own Google Play listing and website on 15 November 2026, linked under Sources. "
          "Data safety labels are written by the developers themselves."),
body="""<p>Linking your bank to a budgeting app is convenient: transactions arrive on their own and categories fill in automatically. It also means a third-party data provider can read your accounts, your transaction history sits on another company&#x27;s servers, and the app stops working well when the connection breaks. For some people, that trade isn&#x27;t worth it.</p>
<p>This guide is for them. It covers why you might skip bank linking, what to check in an app before you trust it with your numbers, and the Android budget apps that work entirely on manual entry.</p>

<h2>Why skip bank linking?</h2>
<ul>
<li><b>Privacy.</b> Linked apps typically use a data aggregator. YNAB, for example, names MX and Plaid as its providers. Your transactions pass through that provider and are stored by the app.</li>
<li><b>Credentials.</b> Many banks now support OAuth, where you sign in with the bank itself, but not all. YNAB&#x27;s help pages note that with some banks you may need to enter your login credentials to link.</li>
<li><b>Fewer moving parts.</b> No broken connections, duplicate transactions or missing imports to sort out.</li>
<li><b>Awareness.</b> This is the argument behind kakeibo, the Japanese ledger method. Typing each purchase yourself makes you notice it in a way an automatic feed doesn&#x27;t.</li>
</ul>
<p>The cost is effort. You&#x27;ll enter every expense, ideally the same day. If you know you won&#x27;t, a linked app that you actually look at may serve you better than a manual one you abandon.</p>

<h2>How to check an app&#x27;s privacy before you install it</h2>
<ol>
<li><b>Read the Data safety section</b> on Google Play. It says whether the developer declares collecting or sharing data, and which types. Remember it&#x27;s self-declared by the developer.</li>
<li><b>Look for &ldquo;Contains ads&rdquo;.</b> Ad-supported apps usually involve advertising SDKs, and their Data safety labels often list device or other IDs.</li>
<li><b>Check whether an account is required.</b> If you must sign up, your data is almost certainly stored on the developer&#x27;s servers for sync.</li>
<li><b>Check the permissions.</b> On the app&#x27;s Play page, open &ldquo;About this app&rdquo; and scroll to App permissions. An app without the &ldquo;full network access&rdquo; (internet) permission can&#x27;t send anything anywhere by itself.</li>
<li><b>Look at backups.</b> A local-only app is only as safe as your backups. Prefer apps that let you export an encrypted file you control.</li>
</ol>

<h2>The options compared</h2>
<div class="table"><table>
<tr><th>App</th><th>Method</th><th>Price</th><th>Account</th><th>Privacy notes</th></tr>
<tr><td>Kakeibo Ledger</td><td>Kakeibo: plan, four boxes, reflect</td><td>Free; Pro US$7.99 once</td><td>No</td><td>Play label: no data collected or shared; no internet permission</td></tr>
<tr><td>Cashew</td><td>Flexible budgets, custom categories</td><td>Free; optional in-app purchases</td><td>No</td><td>Play label: no data collected or shared; optional Google Drive backup</td></tr>
<tr><td>Goodbudget</td><td>Envelopes</td><td>Free plan; Premium US$10/month or US$80/year</td><td>Yes</td><td>Play label: may collect location, personal info and other types; syncs via its servers</td></tr>
<tr><td>Money Manager (Realbyte)</td><td>Double-entry ledger with accounts</td><td>Free with ads; paid upgrade</td><td>No</td><td>Play label: may collect and share some data types; ads in free version</td></tr>
<tr><td>YNAB (unlinked)</td><td>Zero-based budgeting</td><td>US$14.99/month or US$109/year</td><td>Yes</td><td>Budget stored in YNAB&#x27;s cloud</td></tr>
</table></div>
<p class="note">From each app&#x27;s Google Play listing and website on 15 November 2026. Prices in US dollars.</p>

<h3>Kakeibo Ledger</h3>
<p>Our app, so read this with that in mind. It follows the kakeibo method: plan the month, write each expense in one of four boxes (needs, wants, culture, unexpected), reflect at month end. It doesn&#x27;t request Android&#x27;s internet permission, so it can&#x27;t go online; purchases go through the Google Play app on your phone. No account, no ads, no analytics. Backups are free, encrypted with a passphrase you choose, and saved wherever you pick through Android&#x27;s share sheet. Free covers the whole method with the last three months of history; Pro (US$7.99, one time) adds unlimited history, a year in review, app lock, CSV export and themes.</p>
<p><b>Not for you if:</b> you want custom categories, multiple currencies, account balances, or sync between devices or with a partner.</p>

<h3>Cashew</h3>
<p>A free, open-source (GPL-3.0) budget and expense tracker for Android, iOS and the web. Its listing says data stays on your device, with optional automatic Google Drive backups, and its Data safety label declares no data collected or shared. It&#x27;s far more flexible than a kakeibo app: custom categories, budgets by week, month or any period, charts, multiple currencies with exchange rates, and bill reminders. It has a 4.8-star rating from about 28,000 reviews.</p>
<p><b>Not for you if:</b> you want a guided method rather than a toolkit. The flexibility that makes Cashew great can also lead to the thirty-category setup that kakeibo tries to avoid.</p>

<h3>Goodbudget</h3>
<p>A long-running envelope budgeting app. The free plan (10 regular and 10 &ldquo;more&rdquo; envelopes, one account, two devices, one year of history) is manual entry only; automatic bank sync is a Premium feature that Goodbudget lists for US banks only. Its big strength is sharing: a household can use one budget across Android, iPhone and the web. That requires an account, and your budget is backed up to Goodbudget&#x27;s servers.</p>
<p><b>Not for you if:</b> you want your data to stay on your phone.</p>

<h3>Money Manager (Realbyte)</h3>
<p>One of the most popular manual-entry ledgers on Android, with over 10 million downloads. It uses double-entry bookkeeping, tracks accounts and cards, and has detailed statistics and Excel backups. The free version shows ads and limits you to 15 assets; a paid version removes both. Its Data safety label says it may collect and share some data types.</p>
<p><b>Not for you if:</b> ads or data collection are the reason you&#x27;re avoiding bank-linked apps.</p>

<h3>YNAB, unlinked</h3>
<p>YNAB lets you keep accounts unlinked and enter transactions by hand or import bank files. It&#x27;s the most thorough option here for debts, credit cards and shared budgets. It&#x27;s also a subscription and requires an account, with your budget in YNAB&#x27;s cloud. See <a href="ynab-alternative-no-bank.html">kakeibo vs YNAB</a> for a fuller comparison.</p>

<h3>Also worth a look</h3>
<p><b>Actual Budget</b> is open-source, local-first budgeting software you can run yourself; it works offline and has optional bank sync. It&#x27;s aimed at people comfortable with a little self-hosting rather than a one-tap Play install. And a plain <b>spreadsheet</b> is still the most private option of all; our <a href="kakeibo-template.html">kakeibo template</a> includes a spreadsheet layout.</p>

<h2>Which one should you choose?</h2>
<ul>
<li><b>You want the most privacy and a simple method:</b> Kakeibo Ledger, or a paper ledger.</li>
<li><b>You want a free, flexible tracker with charts:</b> Cashew.</li>
<li><b>You share money with a partner:</b> Goodbudget, or YNAB if you also manage debts.</li>
<li><b>You want accounts and bookkeeping detail and don&#x27;t mind ads:</b> Money Manager.</li>
</ul>

<h2>Making manual entry stick</h2>
<p>Whichever app you choose, manual budgeting succeeds or fails on habit. Enter purchases the same day, check your bank statement once a week for anything you missed, and do a short review at month end. Our guide to <a href="track-expenses-by-hand.html">tracking expenses by hand</a> covers the routine in detail.</p>
""",
faqs=[
("Is there a budget app that doesn't connect to your bank?", "Yes. On Android, Kakeibo Ledger, Cashew, Money Manager and Goodbudget's free plan all work with manual entry, and YNAB can be used with unlinked accounts. You enter each expense yourself."),
("Is it safe to link my bank to a budgeting app?", "Many people do so safely, especially with banks that support OAuth sign-in through the bank itself. It does mean a data provider and the app store your transactions. If you'd rather avoid that, use a manual-entry app."),
("How can I tell if an Android app can go online?", "On the app's Google Play page, open About this app and scroll to App permissions. If full network access (the internet permission) isn't listed, the app can't open a network connection itself."),
("What is the most private budgeting app for Android?", "The most private options keep data on the phone, need no account and declare no data collected. Kakeibo Ledger goes furthest by having no internet permission at all; Cashew also declares no data collected and is open source."),
("Are Google Play Data safety labels reliable?", "They are a useful starting point, but they are written by each developer. Permissions, the privacy policy and whether an account is required give you a fuller picture."),
],
sources=[S_KL, S_CASHEW, S_CASHEW_GH, S_GB, S_GB_PLAY, S_MM, S_YNAB_PRICE, S_YNAB_MANUAL, S_YNAB_LINK, S_ACTUAL, S_PLAY_DS],
))

# ---------------------------------------------------------------- 8
GUIDES.append(dict(
slug="track-expenses-by-hand",
h1="How to track expenses by hand (and keep doing it)",
title="How to Track Expenses Manually: A Simple Routine | Kakeibo Ledger",
desc="How to track your expenses by hand without giving up in week two: what to record, where to record it, a daily and weekly routine, handling cards, cash, refunds and shared costs.",
answer=("Record every purchase the same day with three things: the amount, a category and a few words about what it was. "
        "Keep the ledger wherever you pay (a pocket notebook or your phone), use a handful of categories rather than dozens, "
        "check your bank and card statements once a week for anything you missed, and total it up at month end. "
        "Fixed bills can be noted once in a monthly plan rather than entered every time."),
disclose=DISC_STD,
body="""<p>Tracking expenses by hand has a reputation for being tedious, and most people who try it stop within a few weeks. That&#x27;s rarely because it takes too long. It&#x27;s because the system was too complicated, or because they fell behind and couldn&#x27;t catch up. This guide is about a simple routine that survives a busy month.</p>
<p>Canada&#x27;s Financial Consumer Agency suggests tracking everything you buy for a month or two before you make a budget, small purchases included. That&#x27;s a good place to start even if you never do anything fancier.</p>

<h2>Why track by hand at all?</h2>
<p>Your bank app already lists your transactions, so why write them again? Three reasons:</p>
<ul>
<li><b>You notice.</b> Seeing a list scroll by isn&#x27;t the same as writing &ldquo;$6.50, coffee&rdquo; for the fifth time this week. The small act of recording is what changes behaviour. That&#x27;s the core idea of kakeibo, the Japanese household ledger.</li>
<li><b>You categorize honestly.</b> Automatic categories can&#x27;t tell groceries from a bottle of wine on the same receipt. You can.</li>
<li><b>You see everything in one place.</b> Cash, several cards, e-transfers and a partner&#x27;s card end up on one page instead of five apps.</li>
</ul>

<h2>What to record</h2>
<p>For each purchase, three fields are enough:</p>
<ol>
<li><b>Amount.</b> What you actually paid, including tax and tip.</li>
<li><b>Category.</b> One of a small fixed set. Kakeibo uses four: needs, wants, culture and unexpected. If you prefer your own, keep it under eight.</li>
<li><b>Note.</b> A few words: &ldquo;groceries&rdquo;, &ldquo;lunch with Sam&rdquo;, &ldquo;bike tube&rdquo;. This is what makes the month-end review useful.</li>
</ol>
<p>The date is usually implied by where you write it. Resist adding more fields like payment method, merchant or location. Every extra field makes each entry slower and the habit more fragile.</p>

<h2>Where to record it</h2>
<div class="table"><table>
<tr><th>Option</th><th>Works well when</th><th>Common problem</th></tr>
<tr><td>Pocket notebook</td><td>You like paper and carry a bag</td><td>Left at home; totals by hand</td></tr>
<tr><td>Phone notes app</td><td>You want zero setup</td><td>No totals; hard to review</td></tr>
<tr><td>Spreadsheet</td><td>You&#x27;re at a computer most days</td><td>Awkward on a phone at the till</td></tr>
<tr><td>Manual-entry app</td><td>You want speed and totals done for you</td><td>Choosing one that respects your data</td></tr>
</table></div>
<p>Our <a href="kakeibo-template.html">kakeibo template</a> works for the first three. For apps, see <a href="budget-app-without-bank-linking.html">budget apps that don&#x27;t link to your bank</a>.</p>

<h2>A routine that survives a busy month</h2>
<h3>Daily: record within the day</h3>
<p>Write each purchase as you pay, or at least before bed. The test is whether you can remember it without looking anything up. If you can&#x27;t, you&#x27;ve waited too long. Tie it to something you already do: when you put your card away, when you plug your phone in at night.</p>
<h3>Weekly: reconcile and look</h3>
<p>Once a week, ideally the same day, spend ten minutes on two things:</p>
<ul>
<li><b>Check your statements.</b> Open your bank and card apps and scan the week. Anything you forgot (an auto-renewal, a tap at the bus, a refund) goes in now. Manual tracking doesn&#x27;t mean ignoring your bank; it means your bank is the backup, not the source.</li>
<li><b>Compare with the plan.</b> Add up each category. If one is running hot, you still have three weeks to adjust.</li>
</ul>
<h3>Monthly: total and reflect</h3>
<p>At month end, total each category, compare with what you planned, and write down one thing to change. Our <a href="monthly-budget-reflection-questions.html">monthly reflection questions</a> make this a fifteen-minute job.</p>

<h2>Tricky cases</h2>
<p><b>Credit cards.</b> Record the purchase when you make it, not when you pay the card bill. Otherwise you count everything twice, or a month late. The card payment itself isn&#x27;t new spending.</p>
<p><b>Cash.</b> Withdrawing cash isn&#x27;t spending; spending it is. Either record each cash purchase, or, if that&#x27;s impractical, record the withdrawal once as &ldquo;cash, wants&rdquo; (or whichever category it mostly goes to) and accept the rough edge.</p>
<p><b>Refunds and returns.</b> Enter them as a negative amount in the same category as the original purchase, so the category total stays honest.</p>
<p><b>Mixed receipts.</b> Split them. A $92 supermarket shop with $18 of wine is $74 needs and $18 wants. Two quick entries.</p>
<p><b>Shared costs.</b> Record only your share. If you paid $80 for dinner and a friend sent you $40, record $40.</p>
<p><b>Fixed bills.</b> Rent, insurance, phone and subscriptions don&#x27;t need to be entered every month in the daily ledger. Put them in a monthly plan once and leave the daily ledger for spending you can actually change. That&#x27;s how kakeibo handles them.</p>
<p><b>Annual costs.</b> A yearly subscription or car registration lands in one month and distorts it. Either note it as unexpected and move on, or set aside a twelfth of it every month in your plan.</p>

<h2>What to do when you fall behind</h2>
<p>You will miss days. Here&#x27;s the recovery:</p>
<ol>
<li>Don&#x27;t try to reconstruct cash purchases you can&#x27;t remember. Let them go.</li>
<li>Pull card and bank transactions for the missing days from your statements and enter them in one sitting.</li>
<li>Start again from today. A month with a three-day gap is still far more informative than no record at all.</li>
</ol>
<p>The most common way to quit is deciding the month is &ldquo;ruined&rdquo; after a gap. It isn&#x27;t. Totals that are 95% complete still show you where the money went.</p>

<h2>Mistakes that make people quit</h2>
<ul>
<li><b>Too many categories.</b> Twenty categories means twenty decisions a day. Four to eight is plenty.</li>
<li><b>Tracking to the cent across five fields.</b> Speed matters more than precision. Round if you like.</li>
<li><b>Never looking at the totals.</b> Tracking without reviewing is just data entry. The weekly look is what makes it worthwhile.</li>
<li><b>Judging yourself.</b> The point is to see clearly, not to feel bad. An honest ledger with overspending in it is a success.</li>
</ul>

<h2>How long until it&#x27;s a habit?</h2>
<p>Most people find the daily entry becomes automatic after a few weeks, and the first full month is the hardest. Plan to do at least two full months before deciding whether it&#x27;s for you: the first month shows you what you spend, and the second shows whether the changes you chose actually worked.</p>

<h2>Tracking by hand on your phone</h2>
<p>Kakeibo Ledger, which we make, is built around this routine. Each expense is a box (needs, wants, culture or unexpected), an amount on a big keypad, and Save, with Today and Yesterday shortcuts and an optional note. Fixed costs go in the monthly plan once. An optional Sunday reminder shows your week against the plan, and the month-end screen totals everything and asks what you&#x27;ll change. You can edit or delete any entry. There&#x27;s no bank sync and no import, on purpose, and the app has no internet permission.</p>
""",
faqs=[
("What is the easiest way to track expenses manually?", "Record each purchase the same day with just the amount, a category from a short list, and a few words about it. Keep the record wherever you pay, check your statements weekly for anything missed, and total it up at month end."),
("Should I track expenses daily or weekly?", "Record daily, review weekly. Same-day entries are quick and accurate; a weekly ten-minute check against your bank and card statements catches anything you forgot and shows which categories are running hot."),
("How do I track credit card spending by hand?", "Record each purchase when you make it, in its spending category. When you pay the card bill, don't record it again, because the spending is already counted."),
("How many expense categories should I use?", "Fewer than you think. Kakeibo uses four: needs, wants, culture and unexpected. Most people do well with four to eight; more makes each entry slower and the month-end picture harder to read."),
("What if I forget to track expenses for a few days?", "Fill in card and bank transactions from your statements, let go of small cash purchases you can't remember, and start again from today. A month that is mostly complete is still very useful."),
],
sources=[S_FCAC, S_PRT, S_KL],
source_note="Checked on 15 November 2026. This guide is general information, not financial advice.",
))

# ---------------------------------------------------------------- 9
GUIDES.append(dict(
slug="monthly-budget-reflection-questions",
h1="Monthly budget reflection: questions to ask, with a template",
title="Monthly Budget Review Questions and Reflection Template | Kakeibo Ledger",
desc="A monthly budget reflection you can do in 20 minutes: the four kakeibo questions, follow-up questions by category, a worked example and a copy-and-paste template.",
answer=("Start with kakeibo&#x27;s four questions: How much did I have? How much did I want to save? How much did I spend? How can I improve? "
        "Then ask a few follow-ups: which category went over and why, what spending I&#x27;d happily repeat, what I regret, and what&#x27;s coming next month. "
        "Finish with one specific change, written where you&#x27;ll see it when you plan next month. Twenty minutes is enough."),
disclose=DISC_STD,
body="""<p>Tracking spending tells you what happened. Reflection is where you decide what to do about it, and it&#x27;s the step most budgets skip. Kakeibo, the Japanese household ledger method, builds it into every month: you don&#x27;t start a new month until you&#x27;ve looked honestly at the last one.</p>
<p>This guide gives you a simple structure for that monthly review: the four core questions, a set of follow-ups to pick from, an example, and a template to copy.</p>

<h2>Before you start</h2>
<p>Set aside twenty minutes in the first few days of the new month, while the old one is still fresh. You&#x27;ll need:</p>
<ul>
<li>Your plan for the month (income, fixed costs, savings goal, spending budget).</li>
<li>Your spending totals by category, from your ledger, spreadsheet or app.</li>
<li>Your bank and card statements, to check that the totals are complete.</li>
<li>Last month&#x27;s reflection, if you have one, to see whether last month&#x27;s change worked.</li>
</ul>
<p>A quiet table and a cup of tea help more than you&#x27;d think. This isn&#x27;t an audit; it&#x27;s a conversation with yourself.</p>

<h2>The four core questions</h2>
<h3>1. How much did I have?</h3>
<p>Your income for the month, minus fixed costs. This is the money you actually had choices about. If income was different from what you planned (overtime, a late invoice, a bonus), note it.</p>
<h3>2. How much did I want to save?</h3>
<p>The savings goal you set at the start. Write it down even if you missed it; the gap is information.</p>
<h3>3. How much did I spend?</h3>
<p>Your total spending across all categories. Then compare: did what you had, minus what you spent, reach your savings goal?</p>
<h3>4. How can I improve?</h3>
<p>The question that matters. Answer it last, after the follow-ups below, and make the answer one specific, doable change, not a resolution. &ldquo;Spend less on food&rdquo; is a resolution. &ldquo;Bring lunch Monday to Thursday&rdquo; is a change.</p>

<h2>Follow-up questions to choose from</h2>
<p>You don&#x27;t need all of these every month. Pick the three or four that fit what happened.</p>
<h3>About the numbers</h3>
<ul>
<li>Which category went furthest over its budget? What were the three biggest items in it?</li>
<li>Which category came in under? Was that a good choice or just a quiet month?</li>
<li>Were there any unexpected costs? Were they truly unexpected, or something that comes round every year?</li>
<li>How did my total compare with last month, and with the month before?</li>
</ul>
<h3>About how it felt</h3>
<ul>
<li>Which purchase am I gladdest I made?</li>
<li>Which purchase would I undo if I could?</li>
<li>When did I spend without thinking? (Time of day, mood, place, people.)</li>
<li>Did I spend anything on culture, the things that feed my mind? Would I like to?</li>
</ul>
<h3>About next month</h3>
<ul>
<li>What&#x27;s coming up that will cost money: birthdays, renewals, trips, school costs?</li>
<li>Does my plan need to change: a new fixed cost, a different savings goal, a different split between categories?</li>
<li>Did last month&#x27;s change work? Keep it, adjust it, or drop it?</li>
</ul>

<h2>A worked example</h2>
<p>Here&#x27;s what a finished reflection might look like for one person in an ordinary month.</p>
<div class="table"><table>
<tr><th>Question</th><th>Answer</th></tr>
<tr><td>How much did I have?</td><td>$1,900 (income $4,100 minus fixed costs $2,200)</td></tr>
<tr><td>How much did I want to save?</td><td>$500</td></tr>
<tr><td>How much did I spend?</td><td>$1,520: needs $690, wants $560, culture $40, unexpected $230</td></tr>
<tr><td>Savings goal met?</td><td>No: $380 of $500</td></tr>
<tr><td>Which box went over?</td><td>Wants, by $160. Biggest items: concert merch $85, two takeaway nights $74, a lamp $60</td></tr>
<tr><td>Gladdest purchase</td><td>The concert itself (bought last month, fully worth it)</td></tr>
<tr><td>Would undo</td><td>The lamp. Bought on a bad day, still in the box</td></tr>
<tr><td>Unexpected</td><td>Dentist $180. I go every year: should be in the plan</td></tr>
<tr><td>Last month&#x27;s change</td><td>&ldquo;No delivery apps on weeknights&rdquo;: mostly kept, saved roughly $100</td></tr>
<tr><td>Next month</td><td>Two birthdays, car insurance renewal</td></tr>
<tr><td><b>One change</b></td><td>Wait 48 hours before any non-grocery purchase over $40. Keep the delivery rule.</td></tr>
</table></div>
<p>Notice that the change is small, specific and tied to a pattern the numbers revealed (an impulse buy on a bad day). That&#x27;s far more likely to stick than &ldquo;spend less on wants&rdquo;.</p>

<h2>Copy-and-paste template</h2>
<pre>MONTHLY REFLECTION — MONTH: __________

1. How much did I have?          $          (income - fixed costs)
2. How much did I want to save?  $
3. How much did I spend?         $
   Needs $      Wants $      Culture $      Unexpected $
   Savings goal met?  yes / no / partly  (actual saved: $    )

Which category went over, and what were the biggest items?

Gladdest purchase:
Purchase I'd undo:
When did I spend without thinking?

Unexpected costs (truly unexpected, or should they be in the plan?):

Did last month's change work?  keep / adjust / drop

Coming up next month:

4. How can I improve? ONE change for next month:
</pre>
<p>For a printable version with the daily ledger too, see our <a href="kakeibo-template.html">kakeibo template</a>.</p>

<h2>Making the reflection count</h2>
<ul>
<li><b>Write one change, not five.</b> Five changes means none of them get done.</li>
<li><b>Put it where you&#x27;ll see it.</b> At the top of next month&#x27;s plan, in your phone&#x27;s lock-screen note, on the fridge.</li>
<li><b>Be kind.</b> The reflection is for learning, not punishment. A month where you overspent but understood why is a good month for your budget.</li>
<li><b>Look back quarterly.</b> Every three months, read your last three reflections together. Patterns that are invisible month to month (always over in wants around payday, always surprised by the same bill) become obvious.</li>
<li><b>Do a year in review.</b> Once a year, look at twelve months of totals against your plans. It&#x27;s the best moment to reset your savings goal and your split between categories.</li>
</ul>

<h2>If you share money with someone</h2>
<p>Do the four questions together, but let each person answer the follow-ups for their own spending first. Then agree on one shared change. Keep it to twenty minutes and keep it about the numbers, not about blame; the numbers are usually more persuasive than an argument.</p>

<h2>Reflection in Kakeibo Ledger</h2>
<p>In Kakeibo Ledger, which we make, the reflection is built in. When a month ends, a banner on the home screen asks you to close it. The reflection screen fills in the first three answers from your plan and your entries, asks whether you met your savings goal, and gives you a box for the fourth: how you&#x27;ll improve. Your note is there when you plan the next month, and a streak counts how many months in a row you&#x27;ve reflected. Pro adds a year in review that shows twelve months of spending against your plans. It all stays on your phone; the app has no internet permission.</p>
""",
faqs=[
("What questions should I ask in a monthly budget review?", "Start with kakeibo's four: how much did I have, how much did I want to save, how much did I spend, and how can I improve. Then ask which category went over and why, which purchases you're glad of or regret, and what's coming next month."),
("How long should a monthly budget review take?", "About 15 to 30 minutes, ideally in the first few days of the new month while you still remember why the numbers look the way they do."),
("What are the four kakeibo questions?", "How much money do you have? How much would you like to save? How much are you spending? How can you improve?"),
("How do I turn a budget review into real change?", "Pick one specific, doable change rather than several general resolutions, write it at the top of next month's plan, and check at the next review whether it worked."),
("Should I also do a yearly budget review?", "Yes. Once a year, look at twelve months of totals against your plans. It's the best time to reset your savings goal and how you split your spending between categories."),
],
sources=[S_PRT, S_PEN, S_FCAC, S_KL],
source_note="Checked on 15 November 2026. The example is illustrative, not financial advice.",
))

# ---------------------------------------------------------------- 10
GUIDES.append(dict(
slug="best-kakeibo-apps-android",
h1="The best kakeibo apps for Android in 2026",
title="Best Kakeibo Apps for Android (2026): Compared Honestly | Kakeibo Ledger",
desc="Kakeibo apps for Android compared: which follow the real method, what they cost, what their Data safety labels say, and which one fits you. Including when ours isn't the best pick.",
answer=("If you want the full kakeibo method on Android, four apps stand out. Kakeibo Ledger (ours) is free with a one-time US$7.99 Pro and has no internet permission. "
        "Kakeibo: Budget Planner by Halil Apps has the most free features, including widgets, CSV export and a no-spend calendar, with an optional Pro subscription. "
        "Kakeibo: Budget &amp; Expense Log is a one-off US$2.99 purchase with stats and a payday start. "
        "Kakebo by RellowTeam is the most downloaded but is a general expense tracker with ads rather than the kakeibo method."),
disclose=("We make Kakeibo Ledger, one of the apps in this comparison, so weigh our view accordingly. We haven&#x27;t done hands-on testing of the other apps; "
          "their details come from their Google Play listings on 15 November 2026, linked below. Data safety labels are written by each developer."),
body="""<p>Search Google Play for &ldquo;kakeibo&rdquo; and you&#x27;ll find a dozen apps with the name. Some follow the method closely: a monthly plan, four categories and a month-end reflection. Others borrow the word for a general expense tracker. Neither is wrong, but if you came for kakeibo, it helps to know which is which.</p>
<p>Here&#x27;s how we compared them, what each one offers, and which we&#x27;d suggest for different people, including when ours isn&#x27;t the best choice.</p>

<h2>What makes a good kakeibo app</h2>
<ol>
<li><b>It follows the method.</b> A monthly plan with savings set first; the four categories (needs, wants, culture, unexpected); and a month-end reflection with the four questions.</li>
<li><b>Entry is fast.</b> Manual entry is the point of kakeibo, so it has to take seconds, not a form.</li>
<li><b>It respects your data.</b> No bank login required, clear Data safety label, ideally no account.</li>
<li><b>Fair pricing.</b> The core method shouldn&#x27;t sit behind a paywall, and you should know what you&#x27;re paying for.</li>
<li><b>You can get your data out.</b> Backup and restore at minimum, export ideally.</li>
</ol>
<p>If you&#x27;re new to the method itself, read <a href="what-is-kakeibo.html">what is kakeibo</a> first.</p>

<h2>The apps at a glance</h2>
<div class="table"><table>
<tr><th>App</th><th>Follows the method</th><th>Price</th><th>Ads</th><th>Play Data safety label</th><th>Downloads</th></tr>
<tr><td>Kakeibo Ledger (Kan Canada Trading Corp.)</td><td>Yes: plan, four boxes, four questions</td><td>Free; Pro US$7.99 once</td><td>No</td><td>No data collected or shared</td><td>New (Nov 2026)</td></tr>
<tr><td>Kakeibo: Budget Planner (Halil Apps)</td><td>Yes: four pillars, savings first, reflection</td><td>Free; optional Pro subscription</td><td>No</td><td>No data shared; may collect app activity, app performance and device IDs</td><td>1K+</td></tr>
<tr><td>Kakeibo: Budget &amp; Expense Log (Pablo Muñoz García)</td><td>Yes: plan, four categories, 5-step reflection</td><td>US$2.99 to buy</td><td>No</td><td>No data collected or shared</td><td>50+</td></tr>
<tr><td>Kakebo: Track Expense &amp; Budget (RellowTeam)</td><td>Partly: monthly budget, but general categories</td><td>Free; in-app purchases</td><td>Yes</td><td>No data shared; may collect financial info</td><td>100K+</td></tr>
</table></div>
<p class="note">From each app&#x27;s Google Play listing (US store) on 15 November 2026. Prices in US dollars.</p>

<h2>Kakeibo Ledger</h2>
<p><b>Best for:</b> people who want the method as it&#x27;s taught, with the strongest privacy guarantee and no subscription.</p>
<p>Our app. You set up the month with income, fixed costs and a savings goal, and it works out what&#x27;s left to spend and suggests a split across the four boxes (50/25/10/15, which you can change). Entries take two taps after the amount, with Today and Yesterday shortcuts and an optional note. At month end it fills in the first three questions and asks you for the fourth; a streak counts reflected months. There&#x27;s an optional Sunday check-in.</p>
<p>Privacy is the main difference. The app doesn&#x27;t request Android&#x27;s internet permission, so it can&#x27;t go online at all; you can check that in its permission details on Google Play. No account, no ads, no analytics. Backups are free and encrypted with a passphrase you choose.</p>
<p>Free covers the whole method with the last three months of history. Pro is US$7.99 once and adds unlimited history, a year in review, app lock, CSV export and two extra themes.</p>
<p><b>Limits:</b> it&#x27;s brand new, so there are no reviews yet. The four categories are fixed. One currency, no widgets, no sync, and months follow the calendar rather than your payday. CSV export is a Pro feature.</p>

<h2>Kakeibo: Budget Planner (Halil Apps)</h2>
<p><b>Best for:</b> people who want the most features free, including widgets.</p>
<p>A well-designed kakeibo app with the method at its centre: you set savings first, split the rest across four pillars, log expenses and reflect monthly with the four classic questions plus a journal. The free tier is generous. Its listing includes home-screen widgets for remaining budget and quick add, a spending calendar with no-spend days and streaks, CSV export, dark mode, every currency and a daily reminder. A newer feature can prompt you to categorize Google Wallet payments, using notification access you choose to turn on.</p>
<p>Pro is an optional subscription with a free trial for eligible users, and adds a monthly coaching report, month-over-month trends, a recurring-expense finder and CSV import. The listing says financial records stay on your device, with no bank linking or cloud sync; its Data safety label declares no data shared but says the app may collect app activity, app performance and device IDs, and mentions that a payment service processes an anonymous customer ID for subscriptions.</p>
<p><b>Choose it over ours if</b> you want widgets, free CSV export, a no-spend calendar or a wider choice of currencies, and you don&#x27;t mind a subscription for the extras.</p>

<h2>Kakeibo: Budget &amp; Expense Log (Pablo Muñoz García)</h2>
<p><b>Best for:</b> people who&#x27;d rather pay a small amount once and get everything.</p>
<p>The closest app to ours in philosophy. It follows the plan, track, reflect cycle with the four classic categories, a monthly budget wizard, a copy-last-month option and a guided five-step reflection. It adds features we don&#x27;t have: weekly, monthly and yearly statistics, emoji tags across categories, search and filters, 27 currencies, CSV and full SQLite export, and plans that can start on your payday. Its listing says it&#x27;s fully offline with no account, and its Data safety label says no data is collected or shared.</p>
<p>It costs US$2.99 up front, with no free version to try first, and it has a very small user base so far (50+ downloads).</p>
<p><b>Choose it over ours if</b> you want stats, tags, payday-based months or several currencies, and you&#x27;re happy to pay before trying.</p>

<h2>Kakebo: Track Expense &amp; Budget (RellowTeam)</h2>
<p><b>Best for:</b> people who want a familiar, flexible expense tracker and like the kakeibo name.</p>
<p>The most downloaded app for the keyword, with 100K+ downloads and a 4.5-star rating. It&#x27;s a capable expense and budget tracker: income and expenses, accounts, categories, recurring transactions, savings goals, charts and offline use. Reviewers include a traditional kakeibo notebook user who liked its real-time balance and PIN lock.</p>
<p>It doesn&#x27;t follow the method closely: there&#x27;s no fixed four-category structure or month-end reflection in its listing, and some categories and transaction types require the premium upgrade, according to reviews. It shows ads, and its Data safety label says it may collect financial info.</p>
<p><b>Choose it if</b> you want flexibility and a large, established app more than the kakeibo routine.</p>

<h2>Not a kakeibo app, but worth knowing: Cashew</h2>
<p>If what you really want is a private, free budget tracker, Cashew is hard to beat. It&#x27;s open source, rated 4.8 stars from about 28,000 reviews, and its Data safety label declares no data collected or shared. It doesn&#x27;t follow the kakeibo method, but you could set up four categories yourself. See <a href="budget-app-without-bank-linking.html">budget apps that don&#x27;t link to your bank</a> for more options like it.</p>

<h2>Which should you pick?</h2>
<ul>
<li><b>Strict method, maximum privacy, pay once:</b> Kakeibo Ledger.</li>
<li><b>Most free features, widgets, no-spend tracking:</b> Kakeibo: Budget Planner (Halil Apps).</li>
<li><b>Stats, tags, payday months, one small payment:</b> Kakeibo: Budget &amp; Expense Log.</li>
<li><b>A flexible general tracker with the kakeibo name:</b> Kakebo (RellowTeam).</li>
<li><b>No app at all:</b> a notebook and our <a href="kakeibo-template.html">free kakeibo template</a>.</li>
</ul>
<p>Whatever you choose, the app matters less than the routine: write things down the same day, look at the totals once a week, and do the reflection at month end.</p>
""",
faqs=[
("What is the best kakeibo app for Android?", "It depends on what you value. Kakeibo Ledger follows the method strictly and has no internet permission; Halil Apps' Kakeibo: Budget Planner has the most free features; Kakeibo: Budget & Expense Log is a one-time US$2.99 purchase with stats and payday months; RellowTeam's Kakebo is the most downloaded general tracker."),
("Is there a free kakeibo app?", "Yes. Kakeibo Ledger and Halil Apps' Kakeibo: Budget Planner are both free to use, with optional paid upgrades. RellowTeam's Kakebo is free with ads and in-app purchases."),
("Is there a kakeibo app that works offline?", "Several. Kakeibo Ledger has no internet permission at all. Kakeibo: Budget & Expense Log says it is fully offline, and Halil Apps and RellowTeam both say your expense data works offline or stays on your device."),
("Is there a kakeibo app for iPhone?", "Kakeibo Ledger is Android only. There are kakeibo apps on the iPhone App Store, but we haven't compared them in this guide."),
("Do kakeibo apps link to your bank?", "The kakeibo apps compared here don't link to banks; you enter expenses yourself, which is the point of the method. Halil Apps' app can optionally read Google Wallet payment notifications if you turn that on."),
],
sources=[S_KL, S_HALIL, S_PALP, S_RELLOW, S_CASHEW, S_PLAY_DS, S_PRT],
))
