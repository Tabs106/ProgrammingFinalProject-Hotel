# by Hassanat Awodipe, Tabatha Correa and Tamsir Jobe

import pandas as pd
import calendar


def fillnull(bookings):
    """ fill null values """
    bookings['children'] = bookings['children'].fillna(0)
    bookings['agent'] = bookings['agent'].fillna(0)
    bookings['company'] = bookings['company'].fillna(0)


def drop_duplicate(bookings):
    """ remove duplicated entries """
    bookings.drop_duplicates(inplace=True)


def change_date(bookings):
    """ combine date columns into one """
    # convert month name of arrival date to number from full month name
    arrival_month = []
    for month in bookings['arrival_date_month']:
        month_num = list(calendar.month_name).index(month)
        arrival_month.append(month_num)
    bookings['arrival_date_month'] = arrival_month

    # concat the date columns to one
    bookings['arrival_date_year'] = bookings['arrival_date_year'].astype(str) + '-' + bookings[
        'arrival_date_month'].astype(
        str) + '-' + bookings['arrival_date_day_of_month'].astype(str)

    # rename arrival date column
    bookings.rename(columns={'arrival_date_year': 'arrival_date'}, inplace=True)


def drop_column(bookings):
    """ remove the redundant columns """
    bookings.drop(
        columns=['is_canceled', 'lead_time', 'arrival_date_month', 'arrival_date_week_number', 'meal', 'market_segment',
                 'reserved_room_type', 'distribution_channel', 'previous_cancellations',
                 'previous_bookings_not_canceled',
                 'assigned_room_type', 'booking_changes', 'deposit_type', 'agent', 'company', 'days_in_waiting_list',
                 'is_repeated_guest', 'customer_type', 'required_car_parking_spaces', 'total_of_special_requests'],
        inplace=True)


def change_datatype(bookings):
    """ convert attributes to the right datatype"""
    bookings['arrival_date'] = pd.to_datetime(bookings['arrival_date'])
    bookings['reservation_status_date'] = pd.to_datetime(bookings['reservation_status_date'])
    bookings['children'] = bookings['children'].astype(int)


def clean_data(bookings):
    """ combines all cleaning functions """
    fillnull(bookings)
    change_date(bookings)
    drop_column(bookings)
    change_datatype(bookings)
    drop_duplicate(bookings)


if __name__ == "__main__":
    hotel_data = pd.read_csv(r'hotel_bookings.csv', encoding='utf-8')
    clean_data(hotel_data)
    hotel_data.to_csv(r'Submission/datasets/hotel_bookings_clean.csv', index=False)
