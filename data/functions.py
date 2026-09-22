'''
Helper functions for analysis.ipynb: the minion colour scheme and one
function per plot.
'''
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns

# ======================================================================
# Minion colour scheme
MINION_YELLOW = '#FCE029'
GOGGLE_GREY = '#8C8C8C'
MINION_BLUE = '#2B5BA8'
SHOE_BLACK = '#1E1E1E'
EVIL_PURPLE = '#6A3D9A'
AGNES_RED = '#D62828'
EDITH_PINK = '#E86FA8'
MARGO_GREEN = '#2E8B57'
VECTOR_ORANGE = '#F28C28'
MINION_PALETTE = [MINION_BLUE, MINION_YELLOW, GOGGLE_GREY, SHOE_BLACK]
# All 9 colours, ordered so neighbouring colours look clearly different
FULL_PALETTE = [
    MINION_BLUE, VECTOR_ORANGE, MARGO_GREEN, EDITH_PINK, MINION_YELLOW,
    EVIL_PURPLE, AGNES_RED, GOGGLE_GREY, SHOE_BLACK,
]

DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# ======================================================================


def set_minion_theme():
    '''Apply the minion palette and shoe-black text/axes to all charts.'''
    sns.set_theme(style='white', palette=MINION_PALETTE)
    plt.rcParams.update({
        'axes.edgecolor': SHOE_BLACK,
        'axes.labelcolor': SHOE_BLACK,
        'axes.titlecolor': SHOE_BLACK,
        'axes.titleweight': 'bold',
        'xtick.color': SHOE_BLACK,
        'ytick.color': SHOE_BLACK,
    })


def _year_label(visits, year):
    '''Title suffix: the given year, or the data's year range when year is None.'''
    if year is not None:
        return str(year)
    years = visits['Visit Datetime'].dt.year
    return f'{years.min()}-{years.max()}'


def plot_top_minions(visits, colour, year, n=10):
    '''Horizontal bar chart of the n minions with the most visits.'''
    top_minions = visits['Name'].value_counts().head(n)

    _, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_minions.values, y=top_minions.index, orient='h', color=colour, ax=ax)
    ax.bar_label(ax.containers[0], labels=[f'{count:,}' for count in top_minions.values], padding=3, color=SHOE_BLACK)
    ax.margins(x=0.1)  # room for value labels
    ax.set_title(f'Top {n} minions by visits ({_year_label(visits, year)})')
    ax.set_xlabel('Visits')
    ax.xaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,g}'))
    ax.set_ylabel('')
    plt.show()


def plot_visits_by_museum(visits, colour, year):
    '''Horizontal bar chart of visits per museum, labelled with count and share.'''
    museum_visits = visits['Museum'].value_counts()
    museum_share = museum_visits / museum_visits.sum() * 100
    labels = [f'{count:,}\n({share:.1f}%)' for count, share in zip(museum_visits.values, museum_share.values)]

    _, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=museum_visits.values, y=museum_visits.index, orient='h', color=colour, ax=ax)
    ax.bar_label(ax.containers[0], labels=labels, padding=3, color=SHOE_BLACK)
    ax.margins(x=0.1)  # room for value labels
    ax.set_title(f'Visits by museum ({_year_label(visits, year)})')
    ax.set_xlabel('Number of Visits')
    ax.xaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,g}'))
    ax.set_ylabel('')
    plt.show()


def plot_avg_visits_by_day(visits, museum, colour, year):
    '''
    Bar chart of a museum's average visits per day, by day of week.
    Average = visits on that weekday / number of those weekdays in the period.
    '''
    period = pd.date_range(visits['Visit Datetime'].min().normalize(), visits['Visit Datetime'].max().normalize(), freq='D')
    days_in_period = pd.Series(period.dayofweek).value_counts().sort_index()
    museum_visits = visits.loc[visits['Museum'] == museum, 'Visit Datetime']
    visits_by_day = museum_visits.dt.dayofweek.value_counts().reindex(range(7), fill_value=0)
    avg_per_day = visits_by_day / days_in_period

    _, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x=DAYS, y=avg_per_day.values, color=colour, ax=ax)
    ax.bar_label(ax.containers[0], fmt='{:,.1f}', padding=3, color=SHOE_BLACK)
    ax.margins(y=0.12)  # headroom for value labels
    ax.set_title(f'{museum}: Average visits per day, by day of week ({_year_label(visits, year)})')
    ax.set_xlabel('')
    ax.set_ylabel('Average visits per day')
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.1f}'))
    plt.show()


def plot_monthly_visits(visits, museum, colour, year):
    '''Line chart of a museum's visits per month over the whole period.'''
    months = pd.period_range(visits['Visit Datetime'].min(), visits['Visit Datetime'].max(), freq='M')
    museum_visits = visits.loc[visits['Museum'] == museum, 'Visit Datetime']
    monthly_visits = museum_visits.dt.to_period('M').value_counts().reindex(months, fill_value=0)

    _, ax = plt.subplots(figsize=(10, 4))
    # Evenly spaced points, one per month, labelled Jan, Feb, ...
    positions = range(len(monthly_visits))
    sns.lineplot(x=positions, y=monthly_visits.values, color=colour, marker='o', ax=ax)
    ax.set_xticks(positions, monthly_visits.index.strftime('%b'))
    ax.set_title(f'{museum}: Monthly visits ({_year_label(visits, year)})')
    ax.set_xlabel('')
    ax.set_ylabel('Visits')
    ax.set_ylim(0, monthly_visits.max() * 1.15)  # 15% headroom above the highest month
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,g}'))
    plt.show()


def plot_visits_by_nationality(visits, colours, year):
    '''
    2x2 grid of horizontal bar charts, one per museum, of visits by
    nationality, labelled with count and share of that museum's visits.
    Each nationality keeps the same colour in every chart: colours are
    assigned in order of overall visits.
    '''
    nationality_order = visits['Nationality'].value_counts().index
    colour_map = dict(zip(nationality_order, colours))
    museums = sorted(visits['Museum'].unique())

    fig, axes = plt.subplots(2, 2, figsize=(14, 9))
    for ax, museum in zip(axes.flat, museums):
        counts = visits.loc[visits['Museum'] == museum, 'Nationality'].value_counts()
        shares = counts / counts.sum() * 100
        labels = [f'{count:,} ({share:.1f}%)' for count, share in zip(counts.values, shares.values)]

        sns.barplot(x=counts.values, y=counts.index, hue=counts.index, palette=colour_map,
                    orient='h', legend=False, ax=ax)
        for container, label in zip(ax.containers, labels):
            ax.bar_label(container, labels=[label], padding=3, color=SHOE_BLACK)
        ax.margins(x=0.3)  # room for value labels
        ax.set_title(museum)
        ax.set_xlabel('Visits')
        ax.xaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,g}'))
        ax.set_ylabel('')
    for ax in axes.flat[len(museums):]:
        ax.set_visible(False)

    fig.suptitle(f'Visits by nationality ({_year_label(visits, year)})', fontweight='bold', color=SHOE_BLACK)
    fig.tight_layout()
    plt.show()
