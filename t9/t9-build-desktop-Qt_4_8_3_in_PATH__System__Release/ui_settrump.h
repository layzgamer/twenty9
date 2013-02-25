/********************************************************************************
** Form generated from reading UI file 'settrump.ui'
**
** Created: Fri Feb 15 19:43:05 2013
**      by: Qt User Interface Compiler version 4.8.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SETTRUMP_H
#define UI_SETTRUMP_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QVBoxLayout *verticalLayout;
    QLabel *label;
    QHBoxLayout *horizontalLayout;
    QPushButton *Card1;
    QSpacerItem *horizontalSpacer;
    QPushButton *Card2;
    QSpacerItem *horizontalSpacer_2;
    QPushButton *Card3;
    QSpacerItem *horizontalSpacer_3;
    QPushButton *Card4;
    QSpacerItem *horizontalSpacer_4;
    QPushButton *joker;
    QHBoxLayout *horizontalLayout_2;
    QSpacerItem *horizontalSpacer_5;
    QPushButton *SecondHand;
    QSpacerItem *horizontalSpacer_6;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QString::fromUtf8("Dialog"));
        Dialog->resize(472, 203);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(Dialog->sizePolicy().hasHeightForWidth());
        Dialog->setSizePolicy(sizePolicy);
        Dialog->setMaximumSize(QSize(472, 203));
        verticalLayout = new QVBoxLayout(Dialog);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        label = new QLabel(Dialog);
        label->setObjectName(QString::fromUtf8("label"));
        QFont font;
        font.setFamily(QString::fromUtf8("Century Schoolbook L"));
        font.setPointSize(20);
        font.setBold(true);
        font.setWeight(75);
        label->setFont(font);
        label->setAlignment(Qt::AlignCenter);

        verticalLayout->addWidget(label);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setSizeConstraint(QLayout::SetFixedSize);
        Card1 = new QPushButton(Dialog);
        Card1->setObjectName(QString::fromUtf8("Card1"));
        QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(Card1->sizePolicy().hasHeightForWidth());
        Card1->setSizePolicy(sizePolicy1);
        Card1->setMinimumSize(QSize(86, 124));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/cards/cards/c02.png"), QSize(), QIcon::Normal, QIcon::Off);
        Card1->setIcon(icon);
        Card1->setIconSize(QSize(81, 119));

        horizontalLayout->addWidget(Card1);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        Card2 = new QPushButton(Dialog);
        Card2->setObjectName(QString::fromUtf8("Card2"));
        sizePolicy1.setHeightForWidth(Card2->sizePolicy().hasHeightForWidth());
        Card2->setSizePolicy(sizePolicy1);
        Card2->setMinimumSize(QSize(86, 124));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/cards/cards/d02.png"), QSize(), QIcon::Normal, QIcon::Off);
        Card2->setIcon(icon1);
        Card2->setIconSize(QSize(81, 119));

        horizontalLayout->addWidget(Card2);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_2);

        Card3 = new QPushButton(Dialog);
        Card3->setObjectName(QString::fromUtf8("Card3"));
        sizePolicy1.setHeightForWidth(Card3->sizePolicy().hasHeightForWidth());
        Card3->setSizePolicy(sizePolicy1);
        Card3->setMinimumSize(QSize(86, 124));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/cards/cards/h02.png"), QSize(), QIcon::Normal, QIcon::Off);
        Card3->setIcon(icon2);
        Card3->setIconSize(QSize(81, 119));

        horizontalLayout->addWidget(Card3);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_3);

        Card4 = new QPushButton(Dialog);
        Card4->setObjectName(QString::fromUtf8("Card4"));
        sizePolicy1.setHeightForWidth(Card4->sizePolicy().hasHeightForWidth());
        Card4->setSizePolicy(sizePolicy1);
        Card4->setMinimumSize(QSize(86, 124));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/cards/cards/s02.png"), QSize(), QIcon::Normal, QIcon::Off);
        Card4->setIcon(icon3);
        Card4->setIconSize(QSize(81, 119));

        horizontalLayout->addWidget(Card4);

        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_4);

        joker = new QPushButton(Dialog);
        joker->setObjectName(QString::fromUtf8("joker"));
        sizePolicy1.setHeightForWidth(joker->sizePolicy().hasHeightForWidth());
        joker->setSizePolicy(sizePolicy1);
        joker->setMinimumSize(QSize(86, 124));
        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/cards/cards/joker.png"), QSize(), QIcon::Normal, QIcon::Off);
        joker->setIcon(icon4);
        joker->setIconSize(QSize(81, 119));

        horizontalLayout->addWidget(joker);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        horizontalSpacer_5 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_5);

        SecondHand = new QPushButton(Dialog);
        SecondHand->setObjectName(QString::fromUtf8("SecondHand"));

        horizontalLayout_2->addWidget(SecondHand);

        horizontalSpacer_6 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_6);


        verticalLayout->addLayout(horizontalLayout_2);


        retranslateUi(Dialog);

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QApplication::translate("Dialog", "Dialog", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("Dialog", "Set Trump", 0, QApplication::UnicodeUTF8));
        SecondHand->setText(QApplication::translate("Dialog", "Second Hand", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SETTRUMP_H
