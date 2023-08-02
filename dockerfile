FROM python
COPY ./* /home/tiran/
WORKDIR "/home/tiran"
CMD python bulls_cows.py 