from util import *

history_3unrolls_5epochs = {'valid_loss': [1.9623953892143839, 0.82389765346460564, 0.96513882705676712, 0.68837289966128057, 1.0815203299967371, 0.864776404037647, 0.66142787043151219, 0.83255305985521511, 0.44100163123034197, 0.52357746442302489, 0.51031146403886907, 0.58037761560019063, 0.53573322227912223, 0.5327354715468724, 0.58404161618263928, 0.52057204603633211, 0.47516667572286048, 0.48153905286676468, 0.37285204085599843, 0.37744211964967067], 'full_train_acc': [0.74667787383925466, 0.79725024015369517, 0.82746958053154418, 0.79498879282740942, 0.76400896573807087, 0.77805795709254144, 0.8478025936599447, 0.79907140569965118, 0.85204530899776132, 0.87481988472622918, 0.8482428754402831, 0.86207172590458359, 0.88424591738713243, 0.84301953250080119, 0.8790425872558465, 0.87113752801793554, 0.83637528017931806, 0.90107668908101624, 0.868275696445727, 0.90231748318923544], 'valid_acc': [0.75210589651022841, 0.82781789009225759, 0.8443642198154846, 0.79131568391496065, 0.77747693541917173, 0.80736060970717982, 0.8415563578018449, 0.80014039310068064, 0.85328920978740452, 0.88898916967509234, 0.87464901724829625, 0.8686321700762123, 0.88738467709586721, 0.85750100280786168, 0.86772964300040223, 0.90322904131568549, 0.82771760930605609, 0.89761331728840676, 0.89400320898515961, 0.89440433212996451], 'batchly_train_loss': [0.46629867411936926, 0.20306360308206806, 0.18094197422501712, 0.16375787289561991, 0.29056742230275662, 0.10223960571592165, 0.14151415193546421, 0.1340833900010143, 0.21596705249233447, 0.08355311452402743, 0.13030320256029593, 0.10830572859956715, 0.19288676481833431, 0.052034689072874556, 0.074709836260092477, 0.069865833488227849, 0.13262798963731931, 0.084784253707568147, 0.085660533483343529, 0.092662051984638255, 12.022599465381841], 'cumulative_train_loss': [0.46785816801274505, 0.33523985502576176, 0.28375001716121978, 0.25372696188208743, 0.16777808349665951, 0.13495413803051387, 0.13714324166954056, 0.13637764075164402, 0.16602294061623898, 0.12471918798241004, 0.12658259662909047, 0.12200956876515615, 0.10964017341127179, 0.080789346530605433, 0.078760588931991476, 0.076535045451483513, 0.077415986082452537, 0.081106270368820982, 0.082626046714045512, 0.085137140609940321], 'full_train_loss': [1.8228362394705899, 0.970066047658249, 1.0646335563718152, 0.71854816466250293, 1.0344978809378234, 0.94622059293935457, 0.67169092474940462, 0.8775204455131167, 0.58295678537141959, 0.71786396001049335, 0.66919502582431933, 0.83218379606602522, 0.61703123660776193, 0.57718912109302101, 0.72503712298745449, 0.76696337821267457, 0.60101815119900548, 0.50936105533888498, 0.49757851313548918, 0.4220053872582486]}

history_2unrolls_5epochs = {'valid_loss': [1.0385423350255976, 1.0448426849522936, 0.70139893515816443, 1.0380533655705368, 0.52850894890569522, 0.65842687243183629, 0.68805555099616589, 0.7109784190025088, 0.50897181669104175, 0.51304067612647886, 0.57502203936992369, 0.53772684247645608, 0.40052676081326771, 0.45709203774343971, 0.80294929729824249, 0.46489052436842621, 0.61968680835884071, 0.5839718405637363, 0.48282853678720905, 0.71757059876230278], 'full_train_acc': [0.73002721741914955, 0.79853105987832196, 0.82230627601665174, 0.80675632404739073, 0.82616874799871964, 0.76635046429714959, 0.82760967018892251, 0.84550112071725947, 0.85620797310278729, 0.84638168427793969, 0.87407941082293217, 0.88506644252321498, 0.88398575088056186, 0.87283861671469598, 0.85628802433557594, 0.88808837656100026, 0.88228466218379864, 0.88196445725264128, 0.86623439000960933, 0.88190441882804871], 'valid_acc': [0.74498596068993117, 0.81187324508624148, 0.85770156438026379, 0.80024067388688236, 0.85348977135980642, 0.78158844765342805, 0.85138387484957878, 0.88337344564781328, 0.88748495788207082, 0.89229843561973543, 0.87725631768952905, 0.88768551945447394, 0.89259927797834049, 0.88487765744083591, 0.84657039711191318, 0.89640994785399153, 0.90553549939831712, 0.8892900120336944, 0.8851784997994393, 0.89139590854392414], 'batchly_train_loss': [0.53251096631650296, 0.23363321418132704, 0.22658957117196044, 0.15787492201850756, 0.31163923667770954, 0.17303114930057364, 0.14763687625609012, 0.15499692228925535, 0.23048664936514379, 0.12637216100438076, 0.12228827107623723, 0.14057242629203254, 0.16614779583790143, 0.10568877029028835, 0.12146529489910009, 0.11822843092529318, 0.13625401630897058, 0.10574252356271582, 0.074839378962733724, 0.057283581070498239, 22.558241895139474], 'cumulative_train_loss': [0.53429190600318033, 0.38371159290375456, 0.33127932758724954, 0.28789207014719753, 0.18657651061401537, 0.17979252331179085, 0.16906205154681861, 0.16554283655326632, 0.11706040528713159, 0.12172405589677215, 0.12191233682429108, 0.12658124995216621, 0.086947467831543987, 0.096333762886006924, 0.10472025855222267, 0.10810011819519279, 0.094487439313986649, 0.10012437633338359, 0.091686668645736255, 0.083078723464275542], 'full_train_loss': [1.325670168581798, 1.0914513257812262, 0.85900497915434515, 1.0251219054662886, 0.65698317950611074, 0.73198250181437907, 0.81265681662553213, 0.73508739323973171, 0.60277523572433733, 0.60035157982898968, 0.59835285496769575, 0.59870500721006947, 0.40657249192449452, 0.47327608914868252, 0.73142812893307463, 0.53948997404212651, 0.71211082645900126, 0.55956216962022998, 0.60111781473879689, 0.69072332617193388]}

history_1unroll_5epochs = {'valid_loss': [1.2248420023297151, 0.66063325017281027, 0.91263263309861875, 0.75360955498381732, 0.94303916502987728, 0.73009010820467446, 0.56289925307057087, 0.52145512356321233, 0.55261199611543677, 0.35555644798740399, 0.72103380580172627, 0.45029309120792038, 0.4645326310444377, 0.70560202840906394, 0.70740246613435598, 0.49463523827761963, 0.4715342524836546, 0.61991554300857399, 0.57361756439008715, 0.52377003921548959], 'full_train_acc': [0.73689161063080244, 0.78698366954851062, 0.81916426512968366, 0.76168747998719355, 0.81366074287544654, 0.84111831572206619, 0.84167867435159027, 0.8689361191162378, 0.84938360550752656, 0.87439961575408542, 0.86977665706051888, 0.8712375920589176, 0.8629522894652617, 0.85504723022734808, 0.81183957732948786, 0.85872958693564039, 0.88006324047390494, 0.85166506564201361, 0.87007684918348549, 0.87495997438360729], 'valid_acc': [0.76734857601283535, 0.82962294424388272, 0.84596871239470417, 0.83012434817488945, 0.83243080625752008, 0.82450862414761328, 0.85699959887685517, 0.87835940633774579, 0.87444845567589269, 0.89540713999197741, 0.88567990373044481, 0.88537906137184041, 0.87515042117930175, 0.87023666265543564, 0.8056558363417573, 0.8650220617729647, 0.89179703168872826, 0.83624147613317046, 0.8886883273164875, 0.87484957882069891], 'batchly_train_loss': [0.43225392796464074, 0.23669791183907127, 0.17227848734101772, 0.20204827330237132, 0.25122997054765467, 0.14386657924995874, 0.15405858342555137, 0.17386880805064639, 0.23339180656203554, 0.11014865050665507, 0.11005149788304355, 0.12892611755758582, 0.18525383171581236, 0.093916942571285841, 0.13555029333555085, 0.11466817546746462, 0.1884105728834225, 0.075135841911602039, 0.11958068876166512, 0.11900499813712917, 23.807257294645819], 'cumulative_train_loss': [0.43369955983074321, 0.3350342937247302, 0.2807220112830015, 0.26103717275573812, 0.16560409888860714, 0.15471719422818223, 0.1544974130927104, 0.15934430090537141, 0.16756742303096631, 0.13881010791027634, 0.12921324138283499, 0.12914140055916981, 0.11064590149449634, 0.1022674579603341, 0.11337407710668025, 0.11369787152555864, 0.1190449722468848, 0.097053755050582821, 0.1045710855437136, 0.10818257326516864], 'full_train_loss': [1.3993240822644959, 0.91394561671272301, 0.99674972238711745, 0.90232882241224899, 0.91459870423121581, 0.70715786391791779, 0.64405995536135763, 0.59167128740672048, 0.69723450861616554, 0.45307413825540932, 0.77847454309450526, 0.53552485356358748, 0.50725429987761372, 0.77251609094317197, 0.75770728843166146, 0.5065721597573164, 0.5513634294633396, 0.54374891321728824, 0.56186000175543072, 0.51530675845382035]}

history_3unrolls_20epochs ={'valid_loss': [1.4424292799223553, 0.86689644197231752, 0.68522504911431326, 0.92943982280126491, 0.87211858321152569, 0.97053116581925358, 1.0813517194397102, 1.1172006795795943, 1.0589097573369413, 0.75241436863317068, 0.59213756910457915, 0.59280242832182883, 1.0787330069458383, 0.44760808559251031, 0.54914012936690626, 0.44750395725968994, 0.97742389453084166, 0.77749146790273427, 0.64249093860295459, 0.60883482987450965, 0.5011661779062776, 0.5713424280861531, 0.60051259274970736, 0.48577551588134549, 0.38801423825932391, 0.85064286863604388, 0.69011457978596169, 0.5573600786327132, 0.60386819781778922, 0.43418336419393727, 0.75860844154179319, 0.45034960126192136, 0.50969099428156539, 0.56109452756367184, 0.3992728216167834, 0.37223222506003628, 0.39209695979021014, 0.3497492988698504, 0.38800295206455776, 0.42321991370534279, 0.37300300151046784, 0.3794227708084294, 0.47984770799857335, 0.45030959150681887, 0.68955424859084202, 0.44296664069552721, 0.38467194910287061, 0.45490506375183287, 0.47494405244270416, 0.35342959036955163, 0.40354547518054795, 0.44950369344567032, 0.49712734559531779, 0.60983822354083117, 0.50037782543057174, 0.42684458740435166, 0.37601343319856373, 0.42821849079679725, 0.41678813823985161, 0.34046474356818307, 0.36069209477543118, 0.34731526962444581, 0.34021102428730426, 0.30886415935096628, 0.37631081733573174, 0.59564594069343135, 0.51840918858474605, 0.44994942164907331, 0.42228244516018365, 0.61621933107051741, 0.41855057154006353, 0.37773160928536043, 0.57654458956257681, 0.29561552603738389, 0.5359929759897033, 0.4231400815303803, 0.43593456230967592, 0.42020324738009507, 0.67265139762714654, 0.5507690712615384], 'full_train_acc': [0.63574687800192076, 0.77355507524815781, 0.78742395132885312, 0.76402897854627172, 0.81001841178354528, 0.85292587255844199, 0.8490433877681709, 0.85222542427153525, 0.85434678194044511, 0.85922990714057834, 0.86413304514889977, 0.85766890810118801, 0.83111191162344356, 0.87674111431316248, 0.87686119116234618, 0.86719500480307632, 0.86175152097342378, 0.87882244636567608, 0.88068363752801992, 0.88984950368235638, 0.88312520012808582, 0.87854226705091443, 0.88930915786103348, 0.84235910983029916, 0.88574687800192342, 0.82184598142811571, 0.88448607108549593, 0.89525296189561354, 0.90762087736151587, 0.8701168747998711, 0.87886247198206624, 0.90828130003201735, 0.87802193403778783, 0.89477265449888133, 0.89443243675953232, 0.884646173551072, 0.88974943964137254, 0.90672030099263057, 0.91224383605506965, 0.87734149855907828, 0.92082933077168894, 0.88460614793467818, 0.89659382004482324, 0.89151056676272711, 0.87514008965738266, 0.88730787704130643, 0.89379202689721204, 0.90393852065321501, 0.92052913864872976, 0.89969580531539883, 0.89395212936279345, 0.8954530899775881, 0.8892291066282435, 0.87485991034262001, 0.89747438360550469, 0.90005603586295024, 0.90425872558437426, 0.88522654498879128, 0.91018251681075457, 0.89823487031699956, 0.90908181235990759, 0.90319804674991966, 0.8931316042267069, 0.90289785462696159, 0.91520573166826036, 0.90511927633685518, 0.90233749599743684, 0.89519292347102331, 0.91280419468459495, 0.89107028498238983, 0.90832132564841805, 0.91566602625680693, 0.89203089977585726, 0.89933557476784998, 0.88322526416906744, 0.91046269612551944, 0.88784822286262954, 0.8881083893692, 0.85768892090938553, 0.91668667947485949], 'valid_acc': [0.63918973124749334, 0.81187324508624104, 0.8143802647412749, 0.78198957079823572, 0.83914961893301043, 0.86512234255916598, 0.85950661853188826, 0.82761732851985392, 0.8550942639390291, 0.85298836742879935, 0.87795828319294034, 0.87525070196550148, 0.840553549939831, 0.88327316486161223, 0.90483353389490551, 0.90804251905335009, 0.84115523465704078, 0.88357400722021495, 0.89219815483353471, 0.90222623345367015, 0.89801444043321288, 0.87986361813076475, 0.9078419574809462, 0.88237063778580238, 0.90112314480545608, 0.85950661853188992, 0.85579622944243916, 0.90724027276373909, 0.9211793020457274, 0.89370236662655378, 0.87434817488969141, 0.92839951865222714, 0.91987565182511144, 0.92168070597673435, 0.92077817890092617, 0.90884476534295999, 0.91827115924589042, 0.9370236662655449, 0.92529081427998572, 0.86421981548335247, 0.93381468110709975, 0.91335740072202243, 0.91626554352186163, 0.89219815483353504, 0.90042117930204579, 0.92418772563176932, 0.93070597673485833, 0.93531889290012171, 0.93391496189330048, 0.91115122342559329, 0.91004813477737678, 0.89279983955074249, 0.91596470116325812, 0.88467709586843213, 0.89981949458483845, 0.92839951865222714, 0.9304051343762535, 0.90453269153630278, 0.9104492579221819, 0.92117930204572951, 0.92539109506618611, 0.91225431207380714, 0.92258323305254886, 0.90342960288808616, 0.9234857601283597, 0.91907340553550121, 0.91004813477737767, 0.90573606097071779, 0.90744083433614087, 0.90914560770156394, 0.90493381468110856, 0.92599277978339456, 0.88618130766145253, 0.92268351383874836, 0.87986361813076497, 0.92428800641797171, 0.89129562775772131, 0.90713999197753947, 0.83092659446449957, 0.89159647011632659], 'batchly_train_loss': [0.64674798688348012, 0.24312245324436021, 0.14376630540513965, 0.13880411850667404, 0.34019808967880372, 0.19584664088843839, 0.1278099120010793, 0.080734409961510697, 0.18874184807947358, 0.13033556765679499, 0.10302556927976486, 0.052108418540867188, 0.14426078447715313, 0.10195350829521484, 0.09810665250233995, 0.071848835794111346, 0.20995228797433182, 0.10709674918037036, 0.12058714421094213, 0.058490630180047361, 0.15940672790141788, 0.06467348405800484, 0.085252668376348026, 0.11236410866219283, 0.13889813106645496, 0.10274968378312833, 0.094671751684996891, 0.074769029272807597, 0.12140215248407124, 0.07801482847992712, 0.081466246864360006, 0.063599784629180756, 0.13695485744901789, 0.072582262292207753, 0.080407694584861328, 0.078974749971230232, 0.12086773107483602, 0.060941180762315417, 0.069136201376015713, 0.071935811987112533, 0.14613924731610714, 0.059386405271444648, 0.077467427452232979, 0.033992761412099108, 0.095356078089390284, 0.11182142317196823, 0.071804531900141716, 0.054897415296289616, 0.10458913507191955, 0.048967562163341721, 0.077407264732869338, 0.073140111885903553, 0.11981292085109697, 0.046943003343197759, 0.072663869799318867, 0.066279718580622107, 0.09365046600215253, 0.06620258187725242, 0.056075412518017238, 0.05622323143035423, 0.073996234291709581, 0.086418735768705027, 0.044567029831434422, 0.042215710230757139, 0.088749275520268983, 0.062481413459866117, 0.037942507566109347, 0.081065585956321948, 0.13568919547960834, 0.052134133672226489, 0.047089412268773237, 0.050335067954801797, 0.099832738650793645, 0.11658946500198408, 0.055658343321287433, 0.060771352694450359, 0.068751804023862939, 0.060659415889993962, 0.058317242754472906, 0.037032557618417082, 6.5281616191838037], 'cumulative_train_loss': [0.64891099018409382, 0.44567800006402691, 0.3449288249831966, 0.29335466990149828, 0.21023737449176746, 0.20302999539160271, 0.17792874398208447, 0.15360989476926357, 0.088625752279846343, 0.10951547617481226, 0.1073497675335283, 0.093527912072478805, 0.091627998918579701, 0.096799372562971331, 0.09723561725908994, 0.090883628568936892, 0.13830942189080556, 0.12267703155168941, 0.12197962754476592, 0.10609414029754688, 0.12009356932278985, 0.092337266185168007, 0.089973106738398242, 0.095575525901983288, 0.091733844634726974, 0.097250959400203438, 0.096390267170434973, 0.090980449514648329, 0.076039439166423528, 0.077028782729113177, 0.078509582774245565, 0.074779024439366917, 0.080289152802940272, 0.076429274416930745, 0.077756889600889806, 0.078061608625995912, 0.078838068598208508, 0.069874685708779485, 0.069628250447567971, 0.070205621975393956, 0.065562379452897918, 0.062469237124958096, 0.067474194964983067, 0.059096855460508343, 0.047181794732487854, 0.079555565236401268, 0.076969013511286766, 0.071446511872838805, 0.050474956033460902, 0.049720000839745072, 0.058959354752912342, 0.062507500824553128, 0.073856053948391426, 0.060377063661983872, 0.064477221438625096, 0.064928221557556801, 0.044629961419135569, 0.055434278843901952, 0.055648227789657931, 0.055792098592167501, 0.044755755440737573, 0.065622022716848194, 0.058595884935286315, 0.054497425876605138, 0.052388547917917423, 0.057443405451447722, 0.050935875567575103, 0.058474585422974658, 0.081211830285135678, 0.066648710111725434, 0.060121691921641227, 0.057672995349454588, 0.05120157635959463, 0.083950101556116916, 0.074509025393214939, 0.071071742816376376, 0.041795278902610027, 0.051243093754388298, 0.053603766390679014, 0.049457508983107211], 'full_train_loss': [2.0163135264800549, 1.0671236049918882, 0.81374761033429155, 0.98460868515553623, 0.92093466347224306, 0.87833602018475476, 0.84970418189026886, 0.89480733340337026, 0.96319316025645663, 0.62905923428852828, 0.56716612105270825, 0.58639542210941609, 1.1177878077891721, 0.46544885382903967, 0.60539070271804307, 0.536511089174741, 0.68353378205899784, 0.61088787349077422, 0.61024589966082987, 0.5433379025097872, 0.54323774432956196, 0.4865898019967772, 0.69300872040038386, 0.67992348108742484, 0.42732696918012258, 0.8938322011181572, 0.58334823222621768, 0.57238169761878666, 0.59736262467035928, 0.48728115904766389, 0.7198059065501915, 0.51211033618399637, 0.55765541898897986, 0.5965977396037645, 0.50267808803387781, 0.44898040927866678, 0.58738563898527418, 0.45083435719437764, 0.39966141588483739, 0.41302458241912232, 0.4859359471044164, 0.43823393424722612, 0.45957743372837317, 0.45202433135658926, 0.81421617625915399, 0.52292730285200928, 0.43952979623907723, 0.59656102444727477, 0.46235135278328804, 0.37040732600087073, 0.46311856149943165, 0.53158704766539866, 0.63373783443890697, 0.61973069673638903, 0.49683582356953881, 0.50643885693544888, 0.53937554995467452, 0.48013125535444784, 0.39591897758718864, 0.45679691019443119, 0.44682851371540655, 0.40987970328309237, 0.63053536175623282, 0.45277047470442483, 0.38890045429313658, 0.6861089879702188, 0.5073949117366503, 0.57471590206557066, 0.43060811885475214, 0.54445138507170621, 0.40288942520737525, 0.36724965512215174, 0.54772074129040249, 0.42873843421739316, 0.553122958692713, 0.49642109880374785, 0.49885270031609047, 0.47250135869171916, 0.73065806130188427, 0.42285769811522422]}

xlabel="batches*300"

plot_loss_acc(history_3unrolls_5epochs["full_train_loss"], history_3unrolls_5epochs["full_train_acc"], history_3unrolls_5epochs["valid_acc"], xlabel=xlabel, attributes={"unrolls":3, "epochs":5})
plot_loss_acc(history_2unrolls_5epochs["full_train_loss"], history_2unrolls_5epochs["full_train_acc"], history_2unrolls_5epochs["valid_acc"], xlabel=xlabel, attributes={"unrolls":2, "epochs":5})
plot_loss_acc(history_1unroll_5epochs["full_train_loss"], history_1unroll_5epochs["full_train_acc"], history_1unroll_5epochs["valid_acc"], xlabel=xlabel, attributes={"unrolls":1, "epochs":5})
plot_loss_acc(history_3unrolls_20epochs["full_train_loss"], history_3unrolls_20epochs["full_train_acc"], history_3unrolls_20epochs["valid_acc"], xlabel=xlabel, attributes={"unrolls":3, "epochs":20})