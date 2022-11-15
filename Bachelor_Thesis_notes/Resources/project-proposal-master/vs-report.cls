%
% Report document class
% for the Institute of Distributed Systems (VS), Uni Ulm
% Stephan Kleber, 2013 - uulm/in/vs/kleber
%
% based on ArsClassica by Lorenzo Pantieri (February 2012), using ClassicThesis
% 	website: http://www.lorenzopantieri.net/
%
%
% usage: change (or renew) general definitions in settings.tex
%
% \documentclass{vs-report}
% \begin{document}
% \makefrontmatter
% 
% YOUR CONTENT
% see ArsClassica and ClassicThesis documentation for special styles
%
% \makebackmatter
% \end{document}

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{vs-report}[2014/10/17 Report document class, Institute of Distributed Systems (VS), Uni Ulm]

\LoadClass[10pt,a4paper,twoside,openany,titlepage,fleqn,%
	BCOR5mm,%  headinclude,footinclude,
	numbers=noenddot,% 
	captions=tableheading]{scrreprt}

\RequirePackage[T1]{fontenc}
\RequirePackage{amsmath,amssymb,amsthm}
\RequirePackage{varioref}
\RequirePackage[backend=biber,style=ieee,hyperref,natbib,minnames=1,maxnames=2,maxcitenames=2,maxbibnames=99]{biblatex} % replace/remove for BibTeX!
% Alternate "beautiful" references: \RequirePackage[backend=biber,style=philosophy-modern,hyperref,square,natbib,minnames=1,maxnames=2,maxcitenames=2,maxbibnames=99]{biblatex}
\RequirePackage{chngpage}
\RequirePackage{calc}
\RequirePackage{listings}
\RequirePackage{graphicx}
\RequirePackage{subfig}
\RequirePackage{multicol}
\RequirePackage{makeidx}
\RequirePackage{fixltx2e}
\RequirePackage{relsize}
\RequirePackage{lipsum}
\RequirePackage{setspace}
\RequirePackage[eulerchapternumbers,subfig,beramono,eulermath,pdfspacing,listings]{classicthesis}
\RequirePackage{arsclassica}
\RequirePackage{enumitem}
\RequirePackage{framed}
\RequirePackage{tikz}

\RequirePackage{csquotes}

%%%% Workaround %%%%
\textheight 675pt
\topmargin -40.58768pt

% ********************************************************************
% options
% ********************************************************************

\newboolean{showLicense}\setboolean{showLicense}{true}
\newboolean{showContents}\setboolean{showContents}{true}
\newboolean{showIndex}\setboolean{showIndex}{false}
\newboolean{showAbstract}\setboolean{showAbstract}{true}

\DeclareOption{full}{
	\setboolean{showContents}{true}
	\setboolean{showIndex}{true}}
\DeclareOption{short}{
	\setboolean{showContents}{false}
	\setboolean{showIndex}{false}}
\DeclareOption{noLicense}{\setboolean{showLicense}{false}}
\DeclareOption{noAbstract}{\setboolean{showAbstract}{false}}
\ProcessOptions*

% ********************************************************************
% arsclassica-settings
% ********************************************************************
\input{settings}

% ********************************************************************
% hyperref
% ******************************************************************** 
\newcommand{\mail}[1]{\href{mailto:#1}{\texttt{#1}}}


% ********************************************************************
% makeidx, multicol
% ********************************************************************
\let\orgtheindex\theindex
\let\orgendtheindex\endtheindex
\def\theindex{%
	\def\twocolumn{\begin{multicols}{2}}%
	\def\onecolumn{}%
	\clearpage
	\orgtheindex
}
\def\endtheindex{%
	\end{multicols}%
	\orgendtheindex
}

\makeindex


% ********************************************************************
% listings
% ********************************************************************

\definecolor{lightergray}{gray}{0.99}

\lstset{language=[LaTeX]Tex,
    keywordstyle=\color{RoyalBlue},
    basicstyle=\normalfont\ttfamily,
    commentstyle=\color{Emerald}\ttfamily,
    stringstyle=\rmfamily,
    numbers=none,
    numberstyle=\scriptsize,
    stepnumber=5,
    numbersep=8pt,
    showstringspaces=false,
    breaklines=true,
    frameround=ftff,
    frame=lines,
    backgroundcolor=\color{lightergray}
} 

\lstset{	morekeywords=%
        {RequirePackage,newboolean,DeclareOption,setboolean,%
        ProcessOptions,PackageError,ifthenelse,boolean,%
        chapterNumber,sodef,textls,allcapsspacing,%
        MakeTextLowercase,orgtheindex,endtheindex,%
        @ifpackageloaded,undefined,sfdefault,%
        DeclareRobustCommand,spacedallcaps,%
        microtypesetup,MakeTextUppercase,lowsmallcapsspacing,%
        lowsmallcapsspacing,spacedlowsmallcaps,
        spacedlowsmallcaps,lehead,headmark,color,%
        headfont,partname,thepart,titleformat,part,
        titlerule,chapter,thechapter,thesection,%
        subsection,thesubsection,thesubsubsection,%
        paragraph,theparagraph,descriptionlabel,titlespacing,%
        graffito,lineskiplimit,finalhyphendemerits,%
        colorbox,captionsetup,labelitemi,%
        myincludegraphics,hypersetup,setlength,%
        definecolor,lsstyle,textssc,subsubsection,%
        graffito@setup,includegraphics,ifdefined,%
        myTitle,textcopyright,myName,lstset,lstnewenvironment,%
        setkeys,lst@BeginAlsoWriteFile,contentsname,%
        toc@heading,@ppljLaTeX,z@,check@mathfonts,%
        sf@size,ptctitle,mtctitle,stctitle,lst@intname,%
        @empty,math@fontsfalse,@ppljscTeX,@iwonaTeX,%
        @iwonascLaTeX,@ctTeX,tw@,ct@sc,@ctTeX,f@family,%
        f@shape,ct@sc,ctLaTeX,ctLaTeXe,@twoe,@sctwoe,%
        texorpdfstring,m@th,ctTeX,@mkboth,ProvidesPackage,%
        theindex,PackageInfo,PackageWarningNoLine,%
        mtifont,mtcindent,@iwonaLaTeX,@ppljTeX,@iwonascTeX,%
        rohead,orgendtheindex,@ppljscLaTeX,%
        @ifclassloaded,toc@headingbkORrp,backreftwosep,%
        backrefalt,backreflastsep,areaset,pnumfont,%
        arsincludegraphics,ExecuteOptions,PackageWarning,textcolor,%
        MessageBreak,ars@@includegraphics,ifcld@backref,rofoot,formatchapter,%
        if@twoside},
        commentstyle=\color{Emerald}\ttfamily,%
        frame=lines}

\lstset{basicstyle=\normalfont\ttfamily}
\lstset{flexiblecolumns=true}
\lstset{moredelim={[is][\normalfont\itshape]{/*}{*/}}}
\lstset{basicstyle=\normalfont\ttfamily}
\lstset{flexiblecolumns=false}
\lstset{moredelim={[is][\ttfamily]{!?}{?!}}} 
\lstset{escapeinside={�*}{*�}}
\lstset{firstnumber=last}
\lstset{moredelim={[is][\ttfamily]{!?}{?!}}}

\DeclareRobustCommand*{\pacchetto}[1]{{\normalfont\ttfamily#1}%
\index{Pacchetto!#1@\texttt{#1}}%
\index{#1@\texttt{#1}}}

\DeclareRobustCommand*{\bibtex}{\textsc{Bib}\TeX%
\index{bibtex@\textsc{Bib}\protect\TeX}%
}

\DeclareRobustCommand*{\amseuler}{\protect\AmS{} Euler%
\index{AmS Euler@\protect\AmS~Euler}%
\index{Font!AmS Euler@\protect\AmS~Euler}}

\lstnewenvironment{code}% 
{\setkeys{lst}{columns=fullflexible,keepspaces=true}%
\lstset{basicstyle=\small\ttfamily}%
}{}

\lstset{extendedchars} 
\lstnewenvironment{sidebyside}{% 
    \global\let\lst@intname\@empty 
    \setbox\z@=\hbox\bgroup 
    \setkeys{lst}{columns=fullflexible,% 
    linewidth=0.45\linewidth,keepspaces=true,%
    breaklines=true,% 
    breakindent=0pt,%
    boxpos=t,%
    basicstyle=\small\ttfamily
}% 
    \lst@BeginAlsoWriteFile{\jobname.tmp}% 
}{% 
    \lst@EndWriteFile\egroup 
        \begin{center}% 
            \begin{minipage}{0.45\linewidth}% 
                \hbox to\linewidth{\box\z@\hss} 
            \end{minipage}% 
            \qquad 
            \begin{minipage}{0.45\linewidth}%
            \setkeys{lst}{frame=none}% 
                \leavevmode \catcode`\^^M=5\relax 
                \small\input{\jobname.tmp}% 
            \end{minipage}% 
        \end{center}% 
} 

\newcommand{\omissis}{[\dots\negthinspace]}

\graphicspath{{Graphics/}}

\hyphenation{Robert Bring-hurst DejaVu
Bera Mono Vera Classic-Thesis suite Knuth Zapf}

\newcommand{\meta}[1]{$\langle${\normalfont\itshape#1}$\rangle$}
\lstset{escapeinside={�*}{*�}}


\DeclareRobustCommand*{\miktex}{MiK\TeX%
\index{miktex@MiK\protect\TeX}%
}

\DeclareRobustCommand*{\metafont}{\MF%
\index{METAFONT@\protect\MF}%
}

\DeclareRobustCommand*{\metapost}{\MP%
\index{METAPOST@\protect\MP}%
}

\DeclareRobustCommand*{\texlive}{\TeX{}~Live%
\index{texlive@\protect\TeX{}~Live}%
}


% ********************************************************************
% biblatex
% ******************************************************************** 

\bibliography{Bibliography}

\renewcommand{\nameyeardelim}{, }

\defbibheading{bibliography}{%
\clearpage
\manualmark
\phantomsection
\addcontentsline{toc}{chapter}{\tocEntry{\bibname}}
\chapter*{\bibname\markboth{\spacedlowsmallcaps{\bibname}}
{\spacedlowsmallcaps{\bibname}}}}     

  \DeclareCiteCommand{\citeyearpar}[\mkbibparens] 
  {\boolfalse{citetracker}% 
   \boolfalse{pagetracker}% 
   \usebibmacro{prenote}} 
  {\printtext[bibhyperref]{\printfield{year}}} 
  {\multicitedelim} 
  {\usebibmacro{postnote}} 

\makeatletter 
  \DeclareCiteCommand{\citetalias} 
  {\usebibmacro{prenote}} 
  {\usebibmacro{citeindex}% 
   \bibhyperref{\@citealias{\thefield{entrykey}}}} 
  {\multicitedelim} 
  {\usebibmacro{postnote}} 
\makeatother 

\setcounter{biburlnumpenalty}{9000}
\setcounter{biburlucpenalty}{9000}
\setcounter{biburllcpenalty}{9000}


% ********************************************************************
% other commands
% ******************************************************************** 

\newcommand{\ita}[1]{% 
  \begin{otherlanguage*}{italian}#1\end{otherlanguage*}}
  
\DeclareRobustCommand*{\pkgname}[1]{{\normalfont\sffamily#1}%
\index{Package!#1@\textsf{#1}}%
\index{#1@\textsf{#1}}}

\DeclareRobustCommand*{\envname}[1]{{\normalfont\ttfamily#1}%
\index{Environment!#1@\texttt{#1}}%
\index{#1@\texttt{#1}}}

\DeclareRobustCommand*{\optname}[1]{{\normalfont\ttfamily#1}%
\index{Option!#1@\texttt{#1}}%
\index{#1@\texttt{#1}}}

\DeclareRobustCommand*{\clsname}[1]{{\normalfont\sffamily#1}%
\index{Class!#1@\textsf{#1}}%
\index{#1@\textsf{#1}}}

\DeclareRobustCommand*{\cmdname}[1]{\mbox{\lstinline!\\#1!}%
\index{#1@\texttt{\hspace*{-1.2ex}\textbackslash#1}}}

\DeclareRobustCommand*{\classicthesis}{Classic\-Thesis}

\DeclareRobustCommand*{\arsclassica}{{\normalfont\sffamily ArsClassica}}

\DeclareRobustCommand*{\miktex}{MiK\TeX%
\index{miktex@MiK\protect\TeX}}

\DeclareRobustCommand*{\texlive}{\TeX{}~Live%
\index{texlive@\protect\TeX{}~Live}}



% ********************************************************************
% more commands by uulm.de/in/vs
% ******************************************************************** 

\newcommand\cclicense{{\normalfont\sffamily\bfseries CC-BY-SA}}
\IfFileExists{ccicons.sty}{%
\usepackage{ccicons}
\renewcommand\cclicense{\ccbysa}
}


\definecolor{shadecolor}{HTML}{F7CCCC}

\definecolor{uulm}{RGB}{125,154,170}
\definecolor{uulm-akzent}{RGB}{169,162,141}

\definecolor{uulm-in}{RGB}{163,38,56}
\definecolor{uulm-med}{RGB}{38,84,124}
\definecolor{uulm-mawi}{RGB}{86,170,28}
\definecolor{uulm-nawi}{RGB}{189,96,5}


%******************************************************************
% Frontmatter
%******************************************************************
\newcommand\makefrontmatter{
	\pagenumbering{roman}
	
	% Titlepage ********************************************
	\begin{titlepage}
		\pdfbookmark{Titlepage}{Titlepage}
		\changetext{0.12\textwidth}{}{}{((\paperwidth  - \textwidth) / 2) - \oddsidemargin - \hoffset - 1in}{}
		\null\vfill
		\begin{center}
		\large \sffamily

		\bigskip

		\begin{tabular} {ll}
		\parbox{0.2\textwidth}{\hspace{2.5cm}}
		&
		\parbox{0.8\textwidth}{
		{\Large\spacedlowsmallcaps{\myName}}}
		\\
		&
		\bigskip
		\\
		&
		\parbox{0.8\textwidth}{
		\begin{spacing}{1.4}
		\raggedright
		{\huge\spacedlowsmallcaps{\myTitle}}
		\end{spacing}
		}
		\end{tabular}

		\bigskip
		\vspace{7cm}

		\begin{tabular} {cc}
		\parbox{0.2\textwidth}{\hspace{2.5cm}}
		&
		\parbox{0.8\textwidth}{{\Large\spacedlowsmallcaps{\mySubTitle}}} 
        \\ \\
        \parbox{0.2\textwidth}{\hspace{2.5cm}}
        &
        \parbox{0.8\textwidth}{{Supervisor: }\mySupervisor}
        \\
		\end{tabular}

		\vspace{6ex}

		% this substitutes \myGroup
		\parbox{0.763\textwidth}{\includegraphics[width=6cm]{bilingual-color-gradient}}

		\begin{tabular} {cc}
		\parbox{0.2\textwidth}{\hspace{2.5cm}}
		&
		\parbox{0.8\textwidth}{{\normalsize
			\vspace{2ex}
			\myLocation \\
			\myUrl \\
			\myTime}}
		\end{tabular}

		\end{center}

		\vfill
	\end{titlepage}

	\thispagestyle{empty}
	\hfill\vfill\vspace{1cm}\hrule
	
	\bigskip
	\ifthenelse{\boolean{showLicense}}{
		\input{License}
	}{
		\hfill\noindent\small{intentionally left blank}
	}
	% Titlepage (end) ***************************************
	
	\cleardoublepage
	\pagestyle{scrheadings}
	\ifthenelse{\boolean{showAbstract}}{
		\input{Chapters/Abstract}
	}{
%		\hfill\noindent\small{intentionally left blank}
	}	
	% Abstract *********************************************	
	
	\hfill

	\vfill

	\hrule
	\bigskip

	\noindent\myName:
	\textit{\myTitle,} \ifthenelse{\equal{\mySubTitle}{}}{}{\mySubTitle,}
	\textcopyright\ \myTime.

	\medskip
	\noindent{\spacedlowsmallcaps{Website}}: \\
	\myUrl

	\medskip
	\noindent{\spacedlowsmallcaps{E-mail}}: \\
	\myMail
	
	\ifthenelse{\isundefined{\myAddress}}{}{
		\medskip
		\noindent{\spacedlowsmallcaps{Address}}: \\
		\myAddress
	}
	% Abstract (end) ****************************************

	
	\ifthenelse{\boolean{showContents}}{
		\clearpage
		% Contents *********************************************
		\phantomsection
		\pdfbookmark{\contentsname}{tableofcontents}
		\setcounter{tocdepth}{2}
		\begingroup 
			\let\clearpage\relax
			\let\cleardoublepage\relax

			\tableofcontents
		\endgroup
		\markboth{\spacedlowsmallcaps{\contentsname}}{\spacedlowsmallcaps{\contentsname}} 

		\begingroup 
			\let\clearpage\relax
			\let\cleardoublepage\relax
		\endgroup
		% Contents (end) ****************************************
	}{}
	\cleardoublepage
	\pagenumbering{arabic}
}


% *****************************************************************
% Backmatter
%******************************************************************
\newcommand\makebackmatter{
	%\nocite{*}
	\printbibliography

	\ifthenelse{\boolean{showIndex}}{
		\clearpage
		% Index ************************************************
		\manualmark
		\markboth{\spacedlowsmallcaps{\indexname}}{\spacedlowsmallcaps{\indexname}}
		\phantomsection
		\begingroup 
			\let\clearpage\relax
			\let\cleardoublepage\relax
			\let\cleardoublepage\relax
		\pagestyle{scrheadings} 
		\addcontentsline{toc}{chapter}{\tocEntry{\indexname}}
		\printindex
		\endgroup 
		% Index (end) *******************************************
	}{}
}

