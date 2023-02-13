import pandas as pd
import calendar


def fillnull(bookings):
    bookings['children'] = bookings['children'].fillna(0)


def change_date(bookings):
    # convert month name of arrival date to number from full month name
    arrival_month = []
    for month in bookings['arrival_date_month']:
        month_num = list(calendar.month_name).index(month)
        arrival_month.append(month_num)
    bookings['arrival_date_month'] = arrival_month

    # concat the data columns to one
    bookings['arrival_date_year'] = bookings['arrival_date_year'].astype(str) + '-' + bookings[
        'arrival_date_month'].astype(
        str) + '-' + bookings['arrival_date_day_of_month'].astype(str)

    # rename arrival date column
    bookings.rename(columns={'arrival_date_year': 'arrival_date'}, inplace=True)
    bookings = bookings.drop(columns=['arrival_date_week_number', 'arrival_date_month', 'arrival_date_day_of_month'])


def change_datatype(bookings):
    # convert arrival_date_year to datetime datatype
    bookings['arrival_date'] = pd.to_datetime(bookings['arrival_date'])
    bookings['reservation_status_date'] = pd.to_datetime(bookings['reservation_status_date'])
    bookings['children'] = bookings['children'].astype(int)


def clean_data(bookings):
    fillnull(bookings)
    change_date(bookings)
    change_datatype(bookings)


if __name__ == "__main__":
    hotel_data = pd.read_csv(r'hotel_bookings.csv', encoding='utf-8')
    clean_data(hotel_data)
    hotel_data.to_csv(r'Submission/datasets/clean_hotel.csv', index=False)
