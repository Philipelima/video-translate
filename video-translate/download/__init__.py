from pytube import YouTube;

class Download:
    
    def __init__(self, path: str, url: str, extension: str = 'mp4', orderBy: str = 'resolution') -> None:

        self.url       = url
        self.path      = path
        self.extension = extension
        self.orderBy   = orderBy

    def dowload(self):

        youtube = YouTube(self.url)

        streams  = youtube.streams;
        filters  = self.__filters_by_setreams(streams=streams)

        orderBy    = filters.order_by(self.orderBy)
        toDownload = self.__first_order_by_desc(orderBy)

        return toDownload.download(self.path, 'teste.mp4')
    
    def dowload_path(self):
        return self.path

    def __filters_by_setreams(self, streams: any):
        return streams.filter(progressive=True,  file_extension=self.extension)


    def __first_order_by_desc(self, orderBy: any):
        
        videosOrderByDesc = orderBy.desc();
        firstOfDesc       = videosOrderByDesc.first();

        return firstOfDesc;