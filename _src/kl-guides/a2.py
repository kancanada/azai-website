from base import GUIDES
from a1 import DISC_STD, S_NDL, S_PRT, S_PEN, S_FCAC, S_KL

S_OL = ("Open Library: All Your Worth, Elizabeth Warren and Amelia Warren Tyagi (2005)", "https://openlibrary.org/works/OL3008892W")
S_YNAB_PRICE = ("YNAB pricing", "https://www.ynab.com/pricing")
S_YNAB_MANUAL = ("YNAB Help: Adding transactions without Direct Import", "https://support.ynab.com/en_us/adding-transactions-without-direct-import-B1kBALVaxx")
S_YNAB_LINK = ("YNAB Help: Linked accounts in YNAB", "https://support.ynab.com/en_us/linked-accounts-in-ynab-B1991f2Cc")
S_GB = ("Goodbudget plans and pricing", "https://goodbudget.com/signup")
S_GB_PLAY = ("Goodbudget on Google Play", "https://play.google.com/store/apps/details?id=com.dayspringtech.envelopes")
S_CASHEW = ("Cashew on Google Play", "https://play.google.com/store/apps/details?id=com.budget.tracker_app")
S_CASHEW_GH = ("Cashew source code on GitHub", "https://github.com/jameskokoska/Cashew")

# ---------------------------------------------------------------- 3
GUIDES.append(dict(
slug="kakeibo-categories",
h1="The four kakeibo categories, with examples",
title="The 4 Kakeibo Categories Explained, With Examples | Kakeibo Ledger",
desc="Needs, wants, culture and unexpected: what goes in each kakeibo category, 40 everyday examples, the grey areas (phone, gym, gifts, takeaway) and a simple rule for deciding.",
answer=("Kakeibo sorts day-to-day spending into four boxes. <b>Needs</b> are things you&#x27;d pay for in any month: groceries, transport, medicine, basic toiletries. "
        "<b>Wants</b> are optional: eating out, takeaway coffee, clothes you don&#x27;t strictly need, entertainment. "
        "<b>Culture</b> is spending that grows your mind: books, courses, museums, concerts, hobbies. "
        "<b>Unexpected</b> is what no plan saw coming: repairs, medical bills, a last-minute gift. "
        "Fixed costs like rent usually sit in the monthly plan, not in the four boxes."),
disclose=DISC_STD,
body="""<p>The four categories are what make kakeibo feel different from other budgets. Most budgeting apps start you with twenty or thirty categories, and people end up spending more time sorting than noticing. Kakeibo gives you four, and asks a simpler question about each purchase: what kind of spending was this?</p>
<p>This guide explains each category, lists everyday examples, and deals with the grey areas that trip people up. If you&#x27;re new to the method, start with <a href="what-is-kakeibo.html">what is kakeibo</a>.</p>

<h2>The four categories at a glance</h2>
<div class="table"><table>
<tr><th>Category</th><th>The question it answers</th><th>Typical examples</th></tr>
<tr><td><span class="dot needs"></span>Needs</td><td>Would I have to pay for this in a tight month?</td><td>Groceries, fuel, bus fare, prescriptions, laundry, basic toiletries</td></tr>
<tr><td><span class="dot wants"></span>Wants</td><td>Could I skip this without real harm?</td><td>Restaurants, takeaway, coffee out, new clothes, gadgets, games</td></tr>
<tr><td><span class="dot culture"></span>Culture</td><td>Does this feed my mind or a skill?</td><td>Books, courses, museum tickets, concerts, music lessons, hobby supplies</td></tr>
<tr><td><span class="dot unexp"></span>Unexpected</td><td>Did I know this was coming at the start of the month?</td><td>Car or bike repairs, dental work, vet bills, replacing a broken phone, a surprise gift</td></tr>
</table></div>
<p>You&#x27;ll see other names for the same idea. Some books and apps call them survival, optional, culture and extra. The labels matter less than using them the same way every month.</p>

<h2><span class="dot needs"></span>Needs</h2>
<p>Needs are the variable essentials: the things that keep your household running that aren&#x27;t a fixed bill. If you cut them to zero, something would go wrong.</p>
<ul>
<li>Groceries and household supplies (cleaning products, toilet paper)</li>
<li>Fuel, parking, transit fares not covered by a pass</li>
<li>Prescriptions and over-the-counter medicine</li>
<li>Basic toiletries and hygiene</li>
<li>Children&#x27;s essentials: nappies, school supplies, clothes they&#x27;ve outgrown</li>
<li>Work costs you can&#x27;t avoid, such as safety boots or a required uniform</li>
<li>Pet food and routine pet care</li>
</ul>
<p>The trap with needs is that they quietly absorb wants. A grocery run can include $40 of snacks and wine; the &ldquo;need&rdquo; is the food, not every item in the basket. Canada&#x27;s Financial Consumer Agency makes a useful point here: needs differ from person to person, and change over time. A car can be a need in a rural town and a want in a city with good transit. Decide what counts as a need for you, and be consistent.</p>

<h2><span class="dot wants"></span>Wants</h2>
<p>Wants are spending you choose for pleasure or convenience. There&#x27;s nothing wrong with them; kakeibo isn&#x27;t about cutting all wants, it&#x27;s about seeing them clearly.</p>
<ul>
<li>Restaurants, takeaway and food delivery</li>
<li>Coffee, snacks and drinks out</li>
<li>Clothes, shoes and accessories beyond what you need</li>
<li>Gadgets, games, apps and in-app purchases</li>
<li>Bars, nights out, cinema tickets for a blockbuster</li>
<li>Upgrades: the premium version of something you&#x27;d buy anyway</li>
<li>Ride-shares you took because it was easier, not because you had to</li>
</ul>
<p>For most people, wants is the box that goes over. That&#x27;s useful information, not a failure. The month-end question is whether the wants were worth it.</p>

<h2><span class="dot culture"></span>Culture</h2>
<p>Culture is the category that surprises people, and it&#x27;s the one that gives kakeibo its character. It&#x27;s spending on things that make you more knowledgeable, more skilled or more connected to the arts: money spent on who you&#x27;re becoming.</p>
<ul>
<li>Books, e-books, audiobooks, magazines and newspapers</li>
<li>Courses, workshops, language classes, tutoring</li>
<li>Museum, gallery, theatre and concert tickets</li>
<li>Music lessons, instrument strings, art supplies</li>
<li>Hobby materials: yarn, seeds, woodworking tools</li>
<li>Entry fees for a talk, a heritage site or a festival</li>
</ul>
<p>Giving culture its own box does two things. It stops valuable spending from being lumped in with impulse buys, and it makes you notice if you spent nothing on it all month. Some people set a small culture budget on purpose, as a reminder to use it.</p>

<h2><span class="dot unexp"></span>Unexpected</h2>
<p>Unexpected is for costs that weren&#x27;t on your radar when you made the month&#x27;s plan. The test is timing, not size.</p>
<ul>
<li>Car, bike or appliance repairs</li>
<li>Dental work, physio, a vet visit</li>
<li>Replacing something broken or lost</li>
<li>A wedding or birthday gift you forgot about</li>
<li>A parking ticket or late fee</li>
<li>Last-minute travel for a family reason</li>
</ul>
<p>If the same &ldquo;unexpected&rdquo; cost shows up every few months (car maintenance, annual subscriptions, birthday gifts), it isn&#x27;t really unexpected. Put a monthly amount for it in your plan instead, and you&#x27;ll be less surprised next time.</p>

<h2>The grey areas</h2>
<p>These come up in almost every first kakeibo month. There&#x27;s no single right answer, but here&#x27;s a sensible default for each.</p>
<div class="table"><table>
<tr><th>Expense</th><th>Suggested box</th><th>Why</th></tr>
<tr><td>Rent, mortgage, insurance, phone and internet bills</td><td>Plan (fixed costs)</td><td>They&#x27;re the same every month; take them out before you budget the four boxes</td></tr>
<tr><td>Groceries vs a takeaway meal</td><td>Needs vs wants</td><td>Feeding yourself is a need; paying someone else to cook is usually a want</td></tr>
<tr><td>Gym membership</td><td>Plan, or wants</td><td>If it&#x27;s a fixed monthly fee, treat it as a fixed cost. Drop-in classes are a want, or culture if it&#x27;s a skill class</td></tr>
<tr><td>Streaming services</td><td>Plan (fixed) or wants</td><td>Fixed if you keep them all month; the reflection is a good time to ask if they&#x27;re still worth it</td></tr>
<tr><td>A novel vs a textbook</td><td>Culture</td><td>Both feed your mind; a required textbook for a course can go in needs</td></tr>
<tr><td>Birthday gifts</td><td>Wants, or unexpected</td><td>Planned gifts are a want you chose; a forgotten one is unexpected. Better still, budget for them</td></tr>
<tr><td>Children&#x27;s activities</td><td>Culture or needs</td><td>Music or swimming lessons fit culture; school fees and childcare are needs or fixed costs</td></tr>
<tr><td>Haircut</td><td>Needs (basic) or wants (premium)</td><td>Pick one rule and stick to it</td></tr>
<tr><td>Charity donations</td><td>Plan, or culture</td><td>Regular giving belongs in the plan; one-off donations many people put in culture</td></tr>
<tr><td>Extra debt payments</td><td>Plan (savings line)</td><td>Paying down debt is closer to saving than spending</td></tr>
<tr><td>Medical costs</td><td>Needs or unexpected</td><td>A regular prescription is a need; an emergency dentist visit is unexpected</td></tr>
</table></div>

<h2>Three rules for deciding quickly</h2>
<ol>
<li><b>Use the tight-month test.</b> If money were very tight this month, would you still buy it? Yes means needs; no means wants or culture.</li>
<li><b>Ask whether it grows you.</b> If a want also teaches you something or connects you to the arts, culture is the better home.</li>
<li><b>Consistency beats accuracy.</b> It matters less whether your gym goes in wants or culture than that it goes in the same box every month. Otherwise month-to-month comparisons stop meaning anything.</li>
</ol>
<p>And if you&#x27;re stuck at the till, pick one and move on. You can change it at the weekly check-in.</p>

<h2>How to split your budget across the four boxes</h2>
<p>Kakeibo doesn&#x27;t prescribe fixed percentages. A reasonable first guess for your spending money (what&#x27;s left after fixed costs and savings) is about half for needs, a quarter for wants, a tenth for culture and the rest for unexpected. Kakeibo Ledger suggests exactly that starting split: 50%, 25%, 10% and 15%.</p>
<p>Your real numbers will differ. If you live in an expensive city, needs may take more; if you have a car that&#x27;s getting old, unexpected may need more room. After one month you&#x27;ll have actual totals, and the second month&#x27;s split should be built on those, not on a rule of thumb. If you&#x27;re curious how this compares with a percentage-based rule, see <a href="kakeibo-vs-50-30-20.html">kakeibo vs the 50/30/20 rule</a>.</p>

<h2>Why only four?</h2>
<p>Because more categories means more decisions and fewer insights. With thirty categories, the month-end view is a long list where nothing stands out. With four, the picture is immediate: wants went over, culture was empty, unexpected was quiet. That&#x27;s enough to choose one thing to change.</p>
<p>If you want detail inside a box, use the note on each entry (&ldquo;lunch with team&rdquo;, &ldquo;cat food&rdquo;) rather than more categories. The notes are there when you reflect, without making each entry a sorting exercise.</p>

<h2>Using the four boxes in an app</h2>
<p>In Kakeibo Ledger, which we make, the four categories are fixed: you can&#x27;t add, rename or delete them, on purpose. Home shows each box with what you&#x27;ve spent against what you planned, and starting an entry from a box picks that category for you, so most expenses take two taps after the amount. You can add a short note to any entry and edit or delete it later. If you want custom categories and sub-categories, a general expense tracker such as Cashew will suit you better.</p>
""",
faqs=[
("What are the four categories in kakeibo?", "Needs, wants, culture and unexpected. Some books call them survival, optional, culture and extra. Fixed costs such as rent and insurance are usually handled in the monthly plan rather than in the four categories."),
("What goes in the culture category in kakeibo?", "Spending that feeds your mind or a skill: books, magazines, courses, workshops, museum and concert tickets, music lessons and hobby supplies."),
("Is rent a need in kakeibo?", "Rent is a need, but in kakeibo it is usually treated as a fixed cost in the monthly plan, taken out before you budget the four categories. The ledger is for variable, day-to-day spending."),
("Where do gifts go in kakeibo?", "Planned gifts usually go in wants, and forgotten or last-minute gifts in unexpected. If gifts come up every year, set aside a monthly amount in your plan for them."),
("Can I add more categories to kakeibo?", "You can, but the method works best with four. If you want more detail, write a short note on each entry instead of adding categories, so month-end totals stay easy to read."),
],
sources=[S_FCAC, S_PEN, S_KL, S_CASHEW],
source_note="Checked on 15 November 2026. Category suggestions are general guidance, not financial advice.",
))

# ---------------------------------------------------------------- 4
GUIDES.append(dict(
slug="kakeibo-vs-50-30-20",
h1="Kakeibo vs the 50/30/20 rule: which budget fits you?",
title="Kakeibo vs the 50/30/20 Rule: Which Budget Fits You? | Kakeibo Ledger",
desc="Kakeibo vs the 50/30/20 rule compared: where each comes from, how they split your money, a worked example, who each suits, and how to combine them.",
answer=("The 50/30/20 rule, popularized by Elizabeth Warren and Amelia Warren Tyagi in <i>All Your Worth</i> (2005), is a target: about 50% of after-tax income on needs, 30% on wants and 20% on savings and debt. "
        "Kakeibo is a routine: plan the month with savings taken out first, write every expense in four categories, and reflect at month end. "
        "50/30/20 tells you roughly where your money should go; kakeibo shows you where it actually went. Many people use both: 50/30/20 to set the savings goal, kakeibo to track the month."),
disclose=DISC_STD,
body="""<p>&ldquo;Kakeibo or 50/30/20?&rdquo; sounds like a choice between two budgets, but they answer different questions. One is a set of proportions. The other is a habit of writing things down and looking back. Once you see that, it&#x27;s easier to decide which you need, or whether you want both.</p>

<h2>The 50/30/20 rule in brief</h2>
<p>The 50/30/20 rule comes from <i>All Your Worth</i> by Elizabeth Warren and her daughter Amelia Warren Tyagi, first published in 2005. The idea is to divide your after-tax income into three parts:</p>
<ul>
<li><b>50% must-haves:</b> the costs you&#x27;re committed to: housing, utilities, insurance, minimum loan payments, groceries, transport to work.</li>
<li><b>30% wants:</b> everything else you spend on: eating out, holidays, hobbies, shopping.</li>
<li><b>20% savings:</b> emergency savings, retirement, and paying down debt beyond the minimums.</li>
</ul>
<p>Its strength is simplicity. You don&#x27;t need to track every coffee; you need to check that the big blocks are roughly in proportion. If must-haves take 65% of your income, the rule tells you that something structural (rent, a car payment) is squeezing everything else.</p>

<h2>Kakeibo in brief</h2>
<p>Kakeibo comes from the household account book Hani Motoko devised in Japan in 1904. As it&#x27;s usually practised today:</p>
<ul>
<li>At the start of the month you note income, fixed costs and a savings goal, and work out your spending money.</li>
<li>During the month you write down every expense in one of four categories: needs, wants, culture and unexpected.</li>
<li>At month end you answer four questions: how much you had, how much you wanted to save, how much you spent, and how you can improve.</li>
</ul>
<p>Kakeibo has no official percentages. It&#x27;s about awareness and steady adjustment, month after month. The full method is in <a href="what-is-kakeibo.html">what is kakeibo</a>.</p>

<h2>Side by side</h2>
<div class="table"><table>
<tr><th></th><th>50/30/20</th><th>Kakeibo</th></tr>
<tr><td>What it is</td><td>A target split of income</td><td>A monthly routine: plan, write, reflect</td></tr>
<tr><td>Origin</td><td>Warren and Tyagi, <i>All Your Worth</i>, 2005</td><td>Hani Motoko&#x27;s household account book, Japan, 1904</td></tr>
<tr><td>Categories</td><td>Three: must-haves, wants, savings</td><td>Fixed costs and savings in the plan, then four boxes: needs, wants, culture, unexpected</td></tr>
<tr><td>Savings</td><td>20% target, including extra debt payments</td><td>Your own goal, set first each month</td></tr>
<tr><td>Tracking</td><td>Not required; check the big blocks</td><td>Every expense, written by you</td></tr>
<tr><td>Time needed</td><td>An hour to set up, then occasional checks</td><td>A few minutes most days, plus 15&ndash;30 minutes at month end</td></tr>
<tr><td>Best at</td><td>Spotting structural problems: housing too expensive, saving too little</td><td>Spotting behavioural patterns: where the small money goes, and why</td></tr>
<tr><td>Weak at</td><td>Telling you what to change day to day</td><td>Telling you whether your overall proportions are healthy</td></tr>
</table></div>

<h2>The same month, both ways</h2>
<p>Take a household with $5,000 a month after tax.</p>
<h3>With 50/30/20</h3>
<p>The targets are $2,500 for must-haves, $1,500 for wants and $1,000 for savings. Looking at last month&#x27;s statements, must-haves came to $2,900 (rent $1,900, utilities and insurance $400, groceries $450, transit $150), wants to $1,600, and savings to $500. The verdict: must-haves are 58% of income, and savings are half the target. The rule points at a big decision: housing is high, so either income rises, rent falls, or wants have to give way to savings.</p>
<h3>With kakeibo</h3>
<p>The plan: income $5,000, fixed costs $2,450 (rent, utilities, insurance, transit), savings goal $700. Spending money: $1,850. During the month every purchase is written down. At month end: needs (mainly groceries) $480, wants $1,080, culture $60, unexpected $310. Total $1,930, $80 over plan. The notes show that $420 of wants was food delivery on weeknights.</p>
<p>The reflection: &ldquo;Delivery on work nights is the leak. Next month: batch cook on Sundays, delivery once a week.&rdquo; That&#x27;s a specific change the 50/30/20 view could never show you, because it doesn&#x27;t look at individual purchases.</p>
<p>Notice that each method found something real. 50/30/20 found the structural problem (rent and a low savings rate). Kakeibo found the behavioural one (delivery). Neither found both.</p>

<h2>Which one should you use?</h2>
<p><b>Choose 50/30/20 if</b> you want a quick health check, you don&#x27;t want to track daily spending, and your problem is more about the big picture than the details. It&#x27;s also a good starting point if you&#x27;ve never budgeted and want a benchmark.</p>
<p><b>Choose kakeibo if</b> you earn enough on paper but money still disappears, you want to spend more mindfully, or you&#x27;ve tried rule-of-thumb budgets and found they didn&#x27;t change anything day to day.</p>
<p><b>Be careful with 50/30/20 if</b> you live somewhere with high housing costs. Rent alone can take most of the 50% in many cities, and the rule can feel like a verdict you can&#x27;t act on this month. Treat it as a direction to move in over time, not a pass-or-fail test.</p>
<p><b>Be careful with kakeibo if</b> you know you won&#x27;t record things daily. A kakeibo ledger with half the purchases missing is worse than a rough 50/30/20 check, because it gives you false confidence.</p>

<h2>How to combine them</h2>
<p>The two methods fit together well, because 50/30/20 sets the destination and kakeibo handles the journey.</p>
<ol>
<li><b>Use 50/30/20 once a year</b> (or when your income changes) as a health check. Are must-haves near half? Is saving near a fifth? If not, note the gap.</li>
<li><b>Set your kakeibo savings goal from it.</b> If 20% isn&#x27;t realistic yet, pick a step towards it, say 10%, and make that the savings line in every monthly plan.</li>
<li><b>Map the categories.</b> Kakeibo&#x27;s fixed costs plus needs roughly equal 50/30/20&#x27;s must-haves. Wants plus culture roughly equal its wants. Unexpected splits between the two depending on what it was.</li>
<li><b>Run kakeibo month to month</b> to find the specific changes that move you towards the target.</li>
</ol>
<p>A note on the mapping: 50/30/20 counts extra debt repayment as savings. In kakeibo, put extra debt payments in the savings line of your plan, not in the four boxes, so the comparison stays fair.</p>

<h2>Other methods worth knowing</h2>
<p>If neither fits, two other approaches are popular. <b>Zero-based budgeting</b>, used by YNAB, gives every dollar a job before you spend it, across as many categories as you like. <b>Envelope budgeting</b>, used by Goodbudget and by people who literally use cash envelopes, sets a fixed amount per category and stops when the envelope is empty. Kakeibo is lighter than both: fewer categories, no account balances, and more emphasis on reflection. See <a href="ynab-alternative-no-bank.html">kakeibo vs YNAB</a> for that comparison.</p>

<h2>Doing kakeibo on your phone</h2>
<p>Kakeibo Ledger, which we make, runs the kakeibo side of this: a monthly plan with your savings goal taken out first, four boxes for expenses, and the month-end questions with the numbers filled in. It doesn&#x27;t calculate 50/30/20 percentages for you, but the plan screen shows income, fixed costs and savings side by side, which makes the health check easy to do in your head. It&#x27;s free to use, with a one-time Pro purchase, and it doesn&#x27;t go online.</p>
""",
faqs=[
("Who created the 50/30/20 rule?", "It was popularized by Elizabeth Warren and Amelia Warren Tyagi in their book All Your Worth, first published in 2005. It suggests about 50% of after-tax income for must-haves, 30% for wants and 20% for savings and debt repayment."),
("Is kakeibo better than the 50/30/20 rule?", "Neither is better in general. 50/30/20 is a quick target for how income should be split; kakeibo is a monthly habit that shows where money actually went. Kakeibo takes more effort but finds specific changes; 50/30/20 is faster but less detailed."),
("Can I use kakeibo and 50/30/20 together?", "Yes. Use 50/30/20 as a yearly health check and to choose your savings goal, then run kakeibo each month to track spending and find what to change."),
("Does kakeibo have percentages?", "No fixed ones. Kakeibo asks you to set your own savings goal and plan for the month. A common starting split of spending money is about 50% needs, 25% wants, 10% culture and 15% unexpected, adjusted after the first month."),
("Is 50/30/20 realistic with high rent?", "Often not straight away. In high-cost cities housing alone can take most of the 50%. Treat the rule as a direction to move in over time rather than a test you must pass this month."),
],
sources=[S_OL, S_PRT, S_PEN, S_YNAB_MANUAL, S_GB, S_KL],
source_note="Checked on 15 November 2026. The examples are illustrative and not financial advice.",
))

# ---------------------------------------------------------------- 5
GUIDES.append(dict(
slug="ynab-alternative-no-bank",
h1="Kakeibo vs YNAB: a YNAB alternative without bank linking",
title="Kakeibo vs YNAB: A YNAB Alternative Without Bank Linking | Kakeibo Ledger",
desc="Looking for a YNAB alternative that doesn't link to your bank? How YNAB and kakeibo differ, what each costs, when YNAB is still better, and other no-bank options.",
answer=("YNAB doesn&#x27;t actually require bank linking: you can use it with unlinked accounts and enter transactions yourself. What it does require is a subscription (US$14.99 a month or US$109 a year on 15 November 2026, after a 34-day free trial) and an account, with your data in YNAB&#x27;s cloud. "
        "Kakeibo is a lighter alternative: a monthly plan, four spending categories and a month-end reflection, done on paper or in an app. "
        "Pick YNAB if you manage several accounts, debts or a shared household budget; pick kakeibo if you mainly want to see and change where your spending goes."),
disclose=("We make Kakeibo Ledger, a kakeibo app for Android that we mention near the end. We haven&#x27;t used YNAB for this article; "
          "everything about YNAB and Goodbudget comes from their own published pages, linked below."),
body="""<p>People usually search for a YNAB alternative for one of three reasons: the price, the bank connection, or the feeling that YNAB is more system than they need. Kakeibo addresses all three, but it isn&#x27;t a like-for-like replacement. This guide explains what each approach does, what it costs, and when YNAB is still the better choice.</p>

<h2>First, a myth: YNAB doesn&#x27;t require bank linking</h2>
<p>YNAB&#x27;s own help pages describe two ways to get transactions in. You can link an account for Direct Import, which YNAB says works through the data providers MX and Plaid, or you can leave an account unlinked and enter transactions by hand, which YNAB calls the tried-and-true method. You can also download a file from your bank and import it.</p>
<p>So if bank linking is your only objection, you can keep YNAB and simply not link. What you can&#x27;t avoid is the subscription, the YNAB account, and your budget living on YNAB&#x27;s servers so it can sync between your phone and the web.</p>
<p>If you do link, YNAB says that banks supporting OAuth let you sign in directly with the bank, so you don&#x27;t give your banking password to the data provider; with other banks you may need to enter your login credentials. YNAB says it stores transaction details (date, payee, amount) and some account details such as name and balance.</p>

<h2>What YNAB is</h2>
<p>YNAB (You Need A Budget) is zero-based budgeting software. You assign every dollar you currently have to a category before you spend it, and when you overspend in one category you move money from another. It tracks account balances, credit cards and loans, handles irregular &ldquo;true expenses&rdquo; by setting money aside for them every month, and syncs between iOS, Android and the web so a household can share one budget.</p>
<p>It&#x27;s a thorough system, and many people credit it with getting them out of debt. It also asks for a lot of attention: categories to fund, accounts to reconcile, and a learning curve that YNAB supports with its own guides.</p>

<h2>What kakeibo is</h2>
<p>Kakeibo is a Japanese household ledger method dating from 1904. You plan the month (income, fixed costs, savings goal), write every expense in one of four categories (needs, wants, culture, unexpected), and answer four reflection questions at month end. There are no account balances to reconcile and no money to move between categories. It&#x27;s a spending journal with a plan at the start and a review at the end. Read <a href="what-is-kakeibo.html">what is kakeibo</a> for the full method.</p>

<h2>YNAB vs kakeibo at a glance</h2>
<div class="table"><table>
<tr><th></th><th>YNAB</th><th>Kakeibo (paper, sheet or app)</th></tr>
<tr><td>Approach</td><td>Zero-based: every dollar gets a job</td><td>Plan, write every expense, reflect</td></tr>
<tr><td>Categories</td><td>As many as you set up</td><td>Four: needs, wants, culture, unexpected</td></tr>
<tr><td>Accounts and balances</td><td>Yes: chequing, savings, credit cards, loans</td><td>No; it tracks spending against a monthly plan</td></tr>
<tr><td>Bank linking</td><td>Optional (MX and Plaid); unlinked and file import also work</td><td>None; you write each expense yourself</td></tr>
<tr><td>Price</td><td>US$14.99/month or US$109/year after a 34-day trial; free for a year for eligible college students</td><td>Free on paper or a spreadsheet; apps vary</td></tr>
<tr><td>Account needed</td><td>Yes</td><td>No</td></tr>
<tr><td>Where data lives</td><td>YNAB&#x27;s cloud, synced to your devices</td><td>Your notebook, file or phone</td></tr>
<tr><td>Sharing with a partner</td><td>Yes, one budget across devices and the web</td><td>Hard; one ledger, one person, unless you share a spreadsheet</td></tr>
<tr><td>Time needed</td><td>Regular sessions to assign money and reconcile</td><td>A minute a day, 15&ndash;30 minutes at month end</td></tr>
</table></div>
<p class="note">YNAB prices in US dollars from ynab.com on 15 November 2026, plus tax where applicable.</p>

<h2>What YNAB costs over time</h2>
<p>At US$109 a year, three years of YNAB comes to US$327, or about US$540 if you pay monthly. If YNAB is what keeps you out of credit card debt, that&#x27;s good value. If you mainly wanted to see where your money goes, it&#x27;s a lot to pay for a spending diary.</p>
<p>Kakeibo on paper or in a spreadsheet costs nothing. Kakeibo apps range from free with ads to one-time purchases to subscriptions; we compare them in <a href="best-kakeibo-apps-android.html">the best kakeibo apps for Android</a>.</p>

<h2>When YNAB is the better choice</h2>
<ul>
<li>You&#x27;re paying down several debts or credit cards and need to see balances and plans for each.</li>
<li>You share a budget with a partner and want both of you to see the same numbers live.</li>
<li>You have big irregular expenses (annual insurance, car registration, holidays) and want to fund them a little each month in their own categories.</li>
<li>You like detail and want to budget on a computer as well as a phone.</li>
<li>You&#x27;re happy for your budget to live in a company&#x27;s cloud in exchange for sync.</li>
</ul>

<h2>When kakeibo is the better choice</h2>
<ul>
<li>You earn enough but don&#x27;t know where it goes, and you want to notice spending rather than manage accounts.</li>
<li>You don&#x27;t want a subscription for budgeting.</li>
<li>You don&#x27;t want an account, or your financial data on anyone&#x27;s server.</li>
<li>You&#x27;ve tried YNAB and found the system more work than the problem.</li>
<li>You want a monthly ritual of reflection, not just a running total.</li>
</ul>

<h2>Other YNAB alternatives that don&#x27;t need bank linking</h2>
<h3>Goodbudget</h3>
<p>Goodbudget is a digital version of the envelope system. Its free plan, which it says is free forever, includes 10 regular and 10 &ldquo;more&rdquo; envelopes, one account, two devices and a year of history, with manual entry. Premium is US$10 a month or US$80 a year and adds unlimited envelopes and accounts, five devices, seven years of history and automatic bank sync, which Goodbudget lists for US banks only. Your budget syncs through Goodbudget&#x27;s servers, so it needs an account. It&#x27;s a good middle ground if you want envelopes and partner sharing without YNAB&#x27;s price.</p>
<h3>Cashew</h3>
<p>Cashew is a free, open-source expense and budget tracker for Android, iOS and the web. Its Google Play listing says your data stays on your device unless you turn on optional Google Drive backups, and its Data safety label says no data is collected or shared. It has flexible budgets, custom categories, multiple currencies and recurring bills. It&#x27;s a great choice if you want a general-purpose tracker; it doesn&#x27;t follow the kakeibo method.</p>
<h3>A spreadsheet</h3>
<p>Free, private and as simple or complex as you like. Our <a href="kakeibo-template.html">kakeibo template</a> includes a spreadsheet layout.</p>
<p>For a wider list, see <a href="budget-app-without-bank-linking.html">budget apps that don&#x27;t link to your bank</a>.</p>

<h2>Kakeibo Ledger, if you want kakeibo on Android</h2>
<p>Kakeibo Ledger, which we make, follows the kakeibo method: a plan for the month, four fixed boxes, two-tap entry and a month-end reflection with the numbers filled in. It doesn&#x27;t link to banks, has no account and no ads, and doesn&#x27;t have Android&#x27;s internet permission, which you can check in the app&#x27;s permission details on Google Play. Encrypted backups are free and go wherever you choose. The method is free with the last three months of history; Pro is a one-time US$7.99 purchase.</p>
<p>The honest limits: it&#x27;s Android only, it doesn&#x27;t track account balances or debts, it uses one currency, and it doesn&#x27;t sync between devices or people. If you need any of those, YNAB or Goodbudget will serve you better.</p>
""",
faqs=[
("Can you use YNAB without linking your bank?", "Yes. YNAB lets you keep accounts unlinked and enter transactions by hand, or import a file downloaded from your bank. You still need a YNAB subscription and account."),
("How much does YNAB cost?", "On 15 November 2026, YNAB's pricing page listed US$14.99 a month or US$109 a year, with a 34-day free trial and a free year for eligible college students."),
("Is kakeibo a good alternative to YNAB?", "For people who mainly want to understand and change their spending, yes: it is simpler and can be free. For managing several accounts, debts or a shared household budget, YNAB does more."),
("What is the cheapest YNAB alternative?", "A kakeibo notebook or spreadsheet costs nothing. Among apps, Cashew is free, Goodbudget has a free plan with 20 envelopes, and some kakeibo apps are free with a one-time upgrade."),
("Which bank data providers does YNAB use?", "YNAB's help pages name MX and Plaid as the providers for linked accounts. With banks that support OAuth you sign in directly with your bank; with others you may need to enter your login credentials."),
],
sources=[S_YNAB_PRICE, S_YNAB_MANUAL, S_YNAB_LINK, S_GB, S_GB_PLAY, S_CASHEW, S_CASHEW_GH, S_PRT, S_KL],
))
