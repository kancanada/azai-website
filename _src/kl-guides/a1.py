from base import GUIDES

DISC_STD = ("We make Kakeibo Ledger, a kakeibo budget journal for Android that we mention near the end. "
            "Facts about the history of kakeibo and about other books and apps come from the sources linked below.")

S_NDL = ("National Diet Library: Hani Motoko, Portraits of Modern Japanese Historical Figures", "https://www.ndl.go.jp/portrait/e/datas/6008")
S_PRT = ("Fujin no Tomo-sha press release, 6 March 2025 (1904 household account book; in Japanese)", "https://prtimes.jp/main/html/rd/p/000000014.000122533.html")
S_PEN = ("Penguin: Kakeibo: The Japanese Art of Budgeting & Saving Money (2017)", "https://www.penguin.co.uk/books/308816/kakeibo-by-chiba-fumiko/9781405936132")
S_FCAC = ("Financial Consumer Agency of Canada: Make a budget", "https://www.canada.ca/en/financial-consumer-agency/services/make-budget.html")
S_KL = ("Kakeibo Ledger on Google Play", "https://play.google.com/store/apps/details?id=com.kancanada.kakeibo")

# ---------------------------------------------------------------- 1
GUIDES.append(dict(
slug="what-is-kakeibo",
h1="What is kakeibo? How to use the Japanese budgeting method",
title="What Is Kakeibo? How to Use the Japanese Budget Method | Kakeibo Ledger",
desc="What kakeibo is, where it comes from (Hani Motoko, 1904), and how to use the method for your first month: the plan, the four categories and the month-end questions.",
answer=("Kakeibo (家計簿, &ldquo;household ledger&rdquo;) is a Japanese way of budgeting by writing every expense down yourself. "
        "The household account book it&#x27;s named after was devised in 1904 by Hani Motoko, a journalist and magazine publisher. "
        "As it&#x27;s usually taught in English today, you start each month by noting your income, fixed costs and savings goal; "
        "you record each expense in one of four categories (needs, wants, culture, unexpected); and at month end you answer four questions: "
        "how much you had, how much you wanted to save, how much you spent, and how you can improve."),
disclose=DISC_STD,
body="""<p>Most budgeting systems try to take effort out of tracking money. Kakeibo does the opposite. It asks you to write each purchase down by hand, sort it into a small number of boxes, and sit with the totals at the end of the month. The small amount of effort is the point: you can&#x27;t write &ldquo;$14 lunch&rdquo; for the fourth time in a week without noticing.</p>
<p>This guide covers where the method comes from, what it looks like in practice, and how to run your first month, whether you use a notebook, a spreadsheet or an app.</p>

<h2>Where kakeibo comes from</h2>
<p>The word <i>kakeibo</i> (家計簿) simply means a household account book. The version people mean when they talk about &ldquo;the kakeibo method&rdquo; goes back to Hani Motoko (1873&ndash;1957). Japan&#x27;s National Diet Library describes her as the first woman journalist in Japan. With her husband, Hani Yoshikazu, she published the magazine <i>Katei no Tomo</i>, which later became <i>Fujin no Tomo</i> (&ldquo;Women&#x27;s Friend&rdquo;), and in 1921 she co-founded the Jiyu Gakuen school.</p>
<p>Fujin no Tomo-sha, the publisher she founded, says she devised the &ldquo;Hani Motoko household account book&rdquo; in 1904, and it still publishes a version of it every year. That makes it one of the longest-running personal finance tools anywhere, older than the credit card or the spreadsheet.</p>
<p>The method reached English-speaking readers much later, mainly through books such as <i>Kakeibo: The Japanese Art of Budgeting &amp; Saving Money</i>, published by Penguin in 2017. Penguin&#x27;s description sums it up as setting a savings goal each month, noting what you spend, and reflecting on the month before.</p>
<p>One honest caveat: the tidy &ldquo;four categories and four questions&rdquo; version is how kakeibo is usually taught in English-language books and apps. Japanese household ledgers, including the one Hani Motoko designed, tend to use more detailed expense headings and a yearly budget. The spirit is the same; the paperwork is simpler.</p>

<h2>The method in one page</h2>
<p>Kakeibo has three parts, and they follow the month.</p>
<h3>1. Plan, on the first day of the month</h3>
<p>Write down four numbers:</p>
<ul>
<li><b>Income:</b> what will actually land in your account this month, after tax.</li>
<li><b>Fixed costs:</b> the bills that come out no matter what you do: rent or mortgage, insurance, phone, internet, loan payments, subscriptions you&#x27;re keeping.</li>
<li><b>Savings goal:</b> what you want to set aside, decided now, not with whatever is left.</li>
<li><b>Spending money:</b> income minus fixed costs minus savings. This is the money the rest of the month is about.</li>
</ul>
<h3>2. Write, every day you spend</h3>
<p>Each purchase goes in the ledger with the date, a few words about what it was, and the amount, in one of four categories:</p>
<ul>
<li><span class="dot needs"></span><b>Needs:</b> groceries, transport, medicine, the basics you&#x27;d pay for in any month.</li>
<li><span class="dot wants"></span><b>Wants:</b> eating out, shopping, takeaway coffee, things that are nice but optional.</li>
<li><span class="dot culture"></span><b>Culture:</b> books, courses, museums, concerts, hobbies that feed your mind.</li>
<li><span class="dot unexp"></span><b>Unexpected:</b> repairs, a vet bill, a gift you forgot about, anything no plan saw coming.</li>
</ul>
<p>Our guide to <a href="kakeibo-categories.html">the four kakeibo categories</a> has a long list of examples and the grey areas people argue about.</p>
<h3>3. Reflect, at the end of the month</h3>
<p>Answer four questions, in writing:</p>
<ol>
<li>How much did you have?</li>
<li>How much did you want to save?</li>
<li>How much did you spend?</li>
<li>How can you improve?</li>
</ol>
<p>The first three are arithmetic. The fourth is the one that changes things, and it works best as one specific change for next month rather than a general resolution. There&#x27;s a longer list of follow-up questions in our <a href="monthly-budget-reflection-questions.html">monthly reflection guide</a>.</p>

<h2>A worked example</h2>
<p>Here&#x27;s a made-up but realistic month for one person.</p>
<div class="table"><table>
<tr><th>Line</th><th>Amount</th><th>Notes</th></tr>
<tr><td>Take-home income</td><td>$3,800</td><td>Two paycheques</td></tr>
<tr><td>Fixed costs</td><td>$2,050</td><td>Rent $1,600, phone $65, internet $70, insurance $120, transit pass $135, streaming $60</td></tr>
<tr><td>Savings goal</td><td>$400</td><td>Moved to savings on payday</td></tr>
<tr><td>Spending money</td><td>$1,350</td><td>$3,800 &minus; $2,050 &minus; $400</td></tr>
</table></div>
<p>A first split of that $1,350 might be $700 for needs, $350 for wants, $100 for culture and $200 for unexpected. Over the month, the ledger fills up: groceries and pharmacy runs under needs, two dinners out and a jacket under wants, a used book and a pottery class under culture, a cracked phone screen under unexpected.</p>
<p>At month end the totals read: needs $640, wants $520, culture $85, unexpected $180. Total spent: $1,425, which is $75 more than planned. Savings still happened because they came out first, but the overspend had to come from somewhere (in this case, the chequing account buffer).</p>
<p>The reflection might say: &ldquo;Wants went $170 over, almost all of it eating out on Fridays after work. Next month: Friday dinner is fine, but one a fortnight, not every week.&rdquo; That&#x27;s a kakeibo month done properly. Nothing dramatic, one clear lesson, and a specific change.</p>

<h2>How to start your first month</h2>
<ol>
<li><b>Pick your tool.</b> A small notebook you carry, a printed sheet, a spreadsheet or an app. We have a <a href="kakeibo-template.html">free kakeibo template</a> you can print or copy. The best tool is the one you&#x27;ll have with you when you pay.</li>
<li><b>Do the plan with real numbers.</b> Pull up last month&#x27;s bank and card statements to get your fixed costs right. Guessing low on fixed costs is the most common way a first kakeibo month goes wrong.</li>
<li><b>Save first.</b> If you can, move the savings amount on payday. If you can&#x27;t yet, set a small goal you&#x27;ll actually hit. A $50 goal you meet teaches more than a $500 goal you abandon.</li>
<li><b>Write things down the same day.</b> Most people who give up on tracking do so because they fall a week behind and can&#x27;t reconstruct it. Same-day entries take seconds.</li>
<li><b>Check in once a week.</b> A five-minute look on Sunday shows whether one category is running hot while there&#x27;s still time to adjust.</li>
<li><b>Close the month.</b> Do the four questions within a few days of month end, while you still remember why the numbers look the way they do.</li>
</ol>
<p>Expect the first month to be messy. You&#x27;ll misjudge a category or two and forget a few coffees. That&#x27;s normal. The second month&#x27;s plan will be far more accurate because it&#x27;s built on the first month&#x27;s reality.</p>

<h2>Why writing it down works</h2>
<p>Kakeibo&#x27;s main idea is that awareness changes behaviour. When a bank app sorts your spending automatically, you see a pie chart once in a while. When you write each purchase yourself, you meet every one of them. Many people find that simply knowing they&#x27;ll have to record a purchase makes them pause before it.</p>
<p>It isn&#x27;t only a Japanese idea, either. Canada&#x27;s Financial Consumer Agency suggests a similar exercise before you build a budget: track everything you buy for a month or two, including small purchases, and sort it into needs and wants. Kakeibo turns that one-off exercise into a monthly habit with a reflection at the end.</p>
<p>We don&#x27;t want to oversell it. Writing things down won&#x27;t raise your income or cut your rent, and it takes a few minutes most days. What it reliably gives you is an accurate picture, which is the starting point for every other money decision.</p>

<h2>Who kakeibo suits, and who it doesn&#x27;t</h2>
<p><b>It suits you if</b> you don&#x27;t really know where your money goes, you want to spend more deliberately rather than just less, you dislike linking your bank to apps, or you&#x27;ve tried detailed budgeting apps and drowned in categories.</p>
<p><b>It may not suit you if</b> you need to manage several accounts, credit cards and debts together, you share finances with a partner who wants to see everything live, or you know you won&#x27;t record things by hand. In those cases a full budgeting app such as YNAB or Goodbudget may serve you better; we compare them in <a href="ynab-alternative-no-bank.html">kakeibo vs YNAB</a>.</p>
<p>Irregular income isn&#x27;t a dealbreaker. Plan the month on a conservative income figure, and treat anything above it as a bonus to save or spend on purpose.</p>

<h2>Paper, spreadsheet or app?</h2>
<div class="table"><table>
<tr><th>Tool</th><th>Good at</th><th>Watch out for</th></tr>
<tr><td>Notebook</td><td>The most mindful option; nothing to install; easy to personalize</td><td>Totals by hand; easy to leave at home; nothing backs it up</td></tr>
<tr><td>Spreadsheet</td><td>Free, flexible, sums for you, easy to look back over a year</td><td>Hard to use on a phone at the till; easy to over-engineer</td></tr>
<tr><td>Kakeibo app</td><td>Always with you; totals and reflection done for you; reminders</td><td>Check what it does with your data, and whether it follows the method or just borrows the name</td></tr>
</table></div>
<p>We compare the Android options in <a href="best-kakeibo-apps-android.html">the best kakeibo apps for Android</a>.</p>

<h2>Kakeibo Ledger, if you want it on your phone</h2>
<p>Kakeibo Ledger, which we make, follows the method as described above. You set the month&#x27;s plan (income, fixed costs, savings goal) and it works out what&#x27;s left to spend and suggests a split across the four boxes. You type each expense yourself in a couple of taps. At month end it fills in the first three questions from your numbers and asks you for the fourth.</p>
<p>It doesn&#x27;t link to your bank, has no account and no ads, and doesn&#x27;t have Android&#x27;s internet permission, so your numbers stay on your phone. The method is free with the last three months of history; Pro is a one-time US$7.99 purchase that adds unlimited history, a year in review, an app lock, CSV export and themes. It&#x27;s Android only, it tracks one currency, and it doesn&#x27;t sync between devices. If you need those, a notebook or spreadsheet is a better fit.</p>
""",
faqs=[
("Who invented kakeibo?", "The household account book behind the kakeibo method was devised in 1904 by Hani Motoko, a Japanese journalist and the founder of the publisher Fujin no Tomo-sha, which still publishes a version of it."),
("What are the four kakeibo questions?", "How much money do you have? How much would you like to save? How much are you spending? How can you improve? The first three come from your plan and your records; the fourth is a written reflection."),
("What are the four kakeibo categories?", "Needs, wants, culture and unexpected. Needs are essentials like groceries and transport, wants are optional purchases like eating out, culture covers books, courses and hobbies, and unexpected covers repairs, medical costs and other surprises."),
("Do you have to write kakeibo by hand?", "No. Traditional kakeibo is a paper book, but the method works in a spreadsheet or an app. What matters is that you record each expense yourself rather than importing it automatically."),
("Is kakeibo good for beginners?", "Yes. It has only four categories and a short monthly routine, so it is one of the easier budgeting methods to start. Expect the first month to be rough; the second month's plan is built on real numbers."),
],
sources=[S_NDL, S_PRT, S_PEN, S_FCAC, S_KL],
source_note="Facts were checked on 15 November 2026. The worked example is illustrative, not financial advice.",
))

# ---------------------------------------------------------------- 2
GUIDES.append(dict(
slug="kakeibo-template",
h1="Free kakeibo template: print it or copy and paste",
title="Free Kakeibo Template: Printable and Copy-Paste | Kakeibo Ledger",
desc="A free kakeibo template you can print or copy: a monthly plan, a daily ledger with the four categories, weekly totals and the month-end reflection, with a worked example.",
answer=("This page is the template. Print it (the button below prints just the worksheets) or copy the plain-text version into a notes app or document. "
        "It has four parts: a monthly plan (income, fixed costs, savings goal, spending money), a daily ledger with columns for needs, wants, culture and unexpected, "
        "weekly totals, and the four month-end questions. There&#x27;s also a spreadsheet layout with formulas."),
disclose=("We make Kakeibo Ledger, an Android app that does the same job as this template; we mention it at the end. "
          "The template is free to print and copy for personal use, with no sign-up."),
extra_css="PRINT",
body="""<p class="no-print">A kakeibo template doesn&#x27;t need to be fancy. It needs a place to plan the month, a place to write each expense with its category, and a place to look back. Here are all three, in a format you can print on plain paper, copy into a notes app, or rebuild in a spreadsheet.</p>
<p class="no-print">If kakeibo is new to you, read <a href="what-is-kakeibo.html">what is kakeibo</a> first. It takes five minutes and makes the template make sense.</p>
<button class="print-btn" onclick="window.print()">Print the template</button>

<h2>Part 1: The monthly plan</h2>
<p>Fill this in on the first day of the month, or on payday if that suits you better. Use last month&#x27;s statements for fixed costs rather than guessing.</p>
<div class="table sheet"><table>
<tr><th>Month</th><th colspan="2">________________</th></tr>
<tr><td>A. Take-home income this month</td><td>$</td><td>After tax, what will actually arrive</td></tr>
<tr><td>B. Fixed costs</td><td>$</td><td>Rent, bills, insurance, loan payments, subscriptions</td></tr>
<tr><td>C. Savings goal</td><td>$</td><td>Decide it now; move it on payday if you can</td></tr>
<tr><td>D. Spending money (A &minus; B &minus; C)</td><td>$</td><td>What the ledger below is about</td></tr>
<tr><td><span class="dot needs"></span>Needs budget</td><td>$</td><td rowspan="4">Optional: split D across the four boxes. A starting point is 50% needs, 25% wants, 10% culture, 15% unexpected; adjust to your life.</td></tr>
<tr><td><span class="dot wants"></span>Wants budget</td><td>$</td></tr>
<tr><td><span class="dot culture"></span>Culture budget</td><td>$</td></tr>
<tr><td><span class="dot unexp"></span>Unexpected budget</td><td>$</td></tr>
</table></div>
<p class="note no-print">Fixed costs list: rent or mortgage, property tax, home or tenant insurance, car insurance and payment, phone, internet, utilities on a fixed plan, transit pass, childcare, loan and credit card minimums, subscriptions you&#x27;re keeping.</p>

<h2>Part 2: The daily ledger</h2>
<p>One line per purchase, written the same day. Put the amount in exactly one of the four columns. Print as many copies of this page as you need; most people use two or three a month.</p>
<div class="table sheet"><table>
<tr><th>Date</th><th>What</th><th>Needs</th><th>Wants</th><th>Culture</th><th>Unexpected</th></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td><b>Page total</b></td><td></td><td></td><td></td><td></td><td></td></tr>
</table></div>
<p class="no-print">Not sure where something goes? Our guide to <a href="kakeibo-categories.html">the four kakeibo categories</a> covers the usual grey areas, like phone bills, gifts and the gym.</p>

<h2>Part 3: Weekly totals</h2>
<p>Once a week, add up each column and compare it with your budget. This is where you catch a bad week before it becomes a bad month.</p>
<div class="table sheet"><table>
<tr><th>Week</th><th>Needs</th><th>Wants</th><th>Culture</th><th>Unexpected</th><th>Week total</th></tr>
<tr><td>Week 1</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Week 2</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Week 3</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Week 4</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Week 5 (part)</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td><b>Month total</b></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td><b>Budget</b></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td><b>Difference</b></td><td></td><td></td><td></td><td></td><td></td></tr>
</table></div>

<h2>Part 4: The month-end reflection</h2>
<div class="table sheet"><table>
<tr><th>Question</th><th>Answer</th></tr>
<tr><td>1. How much did I have? (income &minus; fixed costs)</td><td>$</td></tr>
<tr><td>2. How much did I want to save?</td><td>$</td></tr>
<tr><td>3. How much did I spend? (month total from Part 3)</td><td>$</td></tr>
<tr><td>Did I meet my savings goal? (1 &minus; 3, compared with 2)</td><td>Yes / No / Partly</td></tr>
<tr><td>Which box went over, and why?</td><td style="height:70px"></td></tr>
<tr><td>What went well?</td><td style="height:70px"></td></tr>
<tr><td>4. How can I improve? One change for next month:</td><td style="height:90px"></td></tr>
</table></div>
<p class="no-print">For more questions to ask yourself, see <a href="monthly-budget-reflection-questions.html">monthly budget reflection questions</a>.</p>

<h2 class="no-print">Copy-and-paste version</h2>
<p class="no-print">For a notes app, a document or an email to yourself. Copy everything in the box, then make one copy per month.</p>
<pre class="no-print">KAKEIBO — MONTH: __________

PLAN
Income (take-home):        $
Fixed costs:               $
Savings goal:              $
Spending money:            $   (income - fixed - savings)
  Needs budget:            $
  Wants budget:            $
  Culture budget:          $
  Unexpected budget:       $

LEDGER   (date | what | box | amount)
N = needs, W = wants, C = culture, U = unexpected
01 | groceries          | N | $
01 | coffee             | W | $
...

WEEKLY TOTALS        N        W        C        U
Week 1
Week 2
Week 3
Week 4
Week 5
Month total
Budget
Difference

REFLECTION
1. How much did I have?
2. How much did I want to save?
3. How much did I spend?
   Savings goal met? yes / no / partly
   Which box went over, and why?
   What went well?
4. How can I improve? One change for next month:
</pre>

<h2 class="no-print">Spreadsheet version</h2>
<p class="no-print">If you&#x27;d rather have the totals done for you, set up a sheet with these columns in row 1: <b>Date</b> (A), <b>What</b> (B), <b>Box</b> (C), <b>Amount</b> (D). Enter one expense per row and type N, W, C or U in the Box column. Then add a small summary block:</p>
<pre class="no-print">        F             G
1   Needs         =SUMIF(C:C,"N",D:D)
2   Wants         =SUMIF(C:C,"W",D:D)
3   Culture       =SUMIF(C:C,"C",D:D)
4   Unexpected    =SUMIF(C:C,"U",D:D)
5   Total         =SUM(G1:G4)</pre>
<p class="no-print">These formulas work in Google Sheets, Excel, LibreOffice Calc and Apple Numbers. Use one tab per month and keep the plan numbers at the top of each tab. Resist the urge to add sub-categories; four boxes is the point.</p>

<h2 class="no-print">How to fill it in: a short example</h2>
<p class="no-print">Say your take-home pay is $3,200, fixed costs are $1,750 and your savings goal is $300. Spending money is $1,150. You might budget $575 for needs, $290 for wants, $115 for culture and $170 for unexpected.</p>
<p class="no-print">On the 3rd you buy groceries for $86.40 (N), a coffee for $5.25 (W) and a paperback for $18 (C). On the 9th your bike needs a $45 repair (U). Each goes on its own line, in its own column. On Sunday you add the columns up: if wants is already at $140 after one week, you know where to ease off.</p>
<p class="no-print">At month end, you copy the totals into Part 4, answer the questions, and write one change. That change goes at the top of next month&#x27;s plan so you see it on day one.</p>

<h2 class="no-print">Tips that make a paper ledger stick</h2>
<ul class="no-print">
<li><b>Keep it where you pay.</b> In your bag, or on your phone. A ledger left at home gets filled in from memory, and memory forgets coffees.</li>
<li><b>Record refunds as negative amounts</b> in the same box as the original purchase.</li>
<li><b>Split mixed receipts.</b> A supermarket trip with groceries and a bottle of wine can be two lines: needs and wants.</li>
<li><b>Don&#x27;t record fixed costs in the ledger.</b> They&#x27;re already in the plan. The ledger is for day-to-day spending.</li>
<li><b>Check your bank statement weekly</b> for card purchases you forgot to write down. See <a href="track-expenses-by-hand.html">how to track expenses by hand</a> for more on this.</li>
</ul>

<h2 class="no-print">The same template, as an app</h2>
<p class="no-print">If paper isn&#x27;t for you, Kakeibo Ledger (which we make) is this template on an Android phone. The monthly plan is a short set of questions, and the app suggests the same 50/25/10/15 starting split, which you can change. Each expense is a tap on a box, the amount and Save. Weekly and monthly totals are worked out for you, and the month-end screen fills in the first three questions and asks you for the fourth. It has no internet permission, no account and no ads. The method is free; Pro is a one-time purchase.</p>
""",
faqs=[
("Is this kakeibo template free?", "Yes. You can print it or copy it for personal use without signing up. The print button prints only the worksheets: the plan, the ledger, the weekly totals and the reflection."),
("What should a kakeibo template include?", "A monthly plan with income, fixed costs, a savings goal and spending money; a daily ledger with columns for needs, wants, culture and unexpected; weekly totals; and the four month-end questions."),
("Should fixed costs go in the kakeibo ledger?", "Usually not. Fixed costs such as rent and insurance are taken out in the monthly plan, so the ledger only tracks day-to-day spending. That keeps the ledger short and focused on the money you can actually change."),
("Can I use the kakeibo template in a spreadsheet?", "Yes. Use columns for date, what, box and amount, type N, W, C or U for the box, and add totals with SUMIF formulas. The formulas on this page work in Google Sheets, Excel, LibreOffice Calc and Numbers."),
("How many ledger pages do I need a month?", "Most people need two or three printed ledger pages a month. If you make many small purchases, print more, or switch to a spreadsheet or app so totals are added for you."),
],
sources=[S_FCAC, S_PEN, S_KL],
source_note="The template on this page is original to Kakeibo Ledger. The example amounts are illustrative, not financial advice.",
))
