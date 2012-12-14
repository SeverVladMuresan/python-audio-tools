#!/usr/bin/python

#Audio Tools, a module and set of tools for manipulating audio data
#Copyright (C) 2007-2012  Brian Langenberger

#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

"""a text strings module"""

#Utility usage
USAGE_AT_CONFIG = u"%prog [options]"
USAGE_CD2TRACK = u"%prog [options] [track #] [track #] ..."
USAGE_CDINFO = u"%prog [options]"
USAGE_CDPLAY = u"%prog [track 1] [track 2] ..."
USAGE_TRACKPLAY = u"%prog [track 1] [track 2] ..."
USAGE_COVERDUMP = u"%prog [-d directory] <track>"
USAGE_COVERTAG = u"%prog [OPTIONS] <track 1> [track 2] ..."
USAGE_COVERVIEW = u"%prog [OPTIONS] [track]"
USAGE_DVDA2TRACK = u"%prog [options] [track #] [track #] ..."
USAGE_DVDAINFO = u"%prog [options]"
USAGE_TRACK2CD = u"%prog [options] <track 1> [track 2] ..."
USAGE_TRACK2TRACK = u"%prog [options] <track 1> [track 2] ..."
USAGE_TRACKCAT = u"%prog [options] [-o output] <track 1> [track 2] ..."
USAGE_TRACKCMP = u"%prog <file 1> <file 2>"
USAGE_TRACKCMP_CDIMAGE = u"<CD image> <track 1> <track 2> ..."
USAGE_TRACKCMP_FILES = u"<track 1> <track 2>"
USAGE_TRACKSPLIT = u"%prog [options] [-d directory] <track>"
USAGE_TRACKINFO = u"%prog [options] <track 1> [track 2] ..."
USAGE_TRACKLENGTH = u"%prog <track 1> [track 2] ..."
USAGE_TRACKLINT = \
    u"%prog [options] [--fix] [--undo] [--db file] <track 1> [track 2] ..."
USAGE_TRACKRENAME = u"%prog [options] <track 1> [track 2] ..."
USAGE_TRACKVERIFY = u"%prog <track 1> [track 2] ..."
USAGE_TRACKTAG = u"%prog [options] <track 1> [track 2] ..."

#Utility Options
OPT_VERBOSE = u"the verbosity level to execute at"
OPT_VERBOSE_AT_CONFIG = u"the new default verbosity level"
OPT_TYPE = u"the type of audio track to create"
OPT_TYPE_AT_CONFIG = u"the default audio type to use, " + \
    u"or the type for a given default quality level"
OPT_TYPE_TRACKVERIFY = u"a type of audio to accept"
OPT_QUALITY = u"the quality to store audio tracks at"
OPT_QUALITY_AT_CONFIG = u"the default quality level for a given audio type"
OPT_DIR = u"the directory to store new audio tracks"
OPT_DIR_IMAGES = u"the directory to store extracted images"
OPT_FORMAT = u"the format string for new filenames"
OPT_METADATA_LOOKUP = u"perform metadata lookup"
OPT_NO_MUSICBRAINZ = u"do not query MusicBrainz for metadata"
OPT_NO_FREEDB = u"do not query FreeDB for metadata"
OPT_INTERACTIVE_METADATA = u"edit metadata interactively"
OPT_INTERACTIVE_OPTIONS = u"edit metadata and output options interactively"
OPT_INTERACTIVE_PLAY = u"play in interactive mode"
OPT_INTERACTIVE_AT_CONFIG = u"edit options interactively"
OPT_OUTPUT_PLAY = u"the method to play audio (choose from: %s)"
OPT_OUTPUT_TRACK2TRACK = u"output filename to use, overriding default and -d"
OPT_OUTPUT_TRACKCAT = u"the output file"
OPT_DEFAULT = u"when multiple choices are available, " + \
    u"select the first one automatically"
OPT_ALBUM_NUMBER = \
    u"the album number of this disc, if it is one of a series of albums"
OPT_ALBUM_TOTAL = \
    u"the total albums of this disc\'s set, if it is one of a series of albums"
OPT_REPLAY_GAIN = u"add ReplayGain metadata to newly created tracks"
OPT_REPLAY_GAIN_TRACKTAG = u"add ReplayGain metadata to tracks"
OPT_NO_REPLAY_GAIN = u"do not add ReplayGain metadata in newly created tracks"
OPT_PLAYBACK_TRACK_GAIN = u"apply track ReplayGain during playback, if present"
OPT_PLAYBACK_ALBUM_GAIN = u"apply album ReplayGain during playback, if present"
OPT_SHUFFLE = u"shuffle tracks"
OPT_PREFIX = u"add a prefix to the output image"
OPT_NO_GTK = u"don't use PyGTK for GUI"
OPT_NO_TKINTER = u"don't use Tkinter for GUI"
OPT_AUDIO_TS = u"location of AUDIO_TS directory"
OPT_DVDA_TITLE = u"DVD-Audio title number to extract tracks from"
OPT_TRACK_START = u"the starting track number of the title being extracted"
OPT_TRACK_TOTAL = \
    u"the total number of tracks, if the extracted title is only a subset"
OPT_SPEED = u"the speed to burn the CD at"
OPT_CUESHEET_TRACK2CD = u"the cuesheet to use for writing tracks"
OPT_JOINT = u"the maximum number of processes to run at a time"
OPT_CUESHEET_TRACKCAT = u"a cuesheet to embed in the output file"
OPT_CUESHEET_TRACKSPLIT = u"the cuesheet to use for splitting track"
OPT_NO_SUMMARY = u"suppress summary output"
OPT_TRACKLINT_FIX = u"perform suggest fixes"
OPT_TRACKLINT_DB = u"undo database file"
OPT_TRACKLINT_UNDO = u"undo performed fixes"
OPT_TRACKTAG_COMMENT_FILE = u"a file containing comment text"
OPT_TRACKTAG_REPLACE = u"completely replace all metadata"
OPT_TRACKTAG_CUESHEET = u"a cuesheet to import or get audio metadata from"
OPT_TRACKTAG_REMOVE_IMAGES = u"remove existing images prior to adding new ones"
OPT_TRACKTAG_FRONT_COVER = u"an image file of the front cover"
OPT_TRACKTAG_BACK_COVER = u"an image file of the back cover"
OPT_TRACKTAG_LEAFLET = u"an image file of a leaflet page"
OPT_TRACKTAG_MEDIA = u"an image file of the media"
OPT_TRACKTAG_OTHER_IMAGE = u"an image file related to the track"
OPT_AT_CONFIG_READ_OFFSET = u"the CD-ROM read offset to use"
OPT_AT_CONFIG_WRITE_OFFSET = u"the CD-ROM write offset to use"
OPT_AT_CONFIG_FS_ENCODING = u"the filesystem's text encoding"
OPT_AT_CONFIG_IO_ENCODING = u"the system's text encoding"
OPT_AT_CONFIG_ID3V2_VERSION = u"which ID3v2 version to use by default, if any"
OPT_AT_CONFIG_ID3V1_VERSION = u"which ID3v1 version to use by default, if any"
OPT_AT_CONFIG_ID3V2_PAD = \
    u"whether or not to pad ID3v2 digit fields to 2 digits"
OPT_CAT_EXTRACTION = u"Extraction Options"
OPT_CAT_CD_LOOKUP = u"CD Lookup Options"
OPT_CAT_DVDA_LOOKUP = u"DVD-A Lookup Options"
OPT_CAT_METADATA = u"Metadata Options"
OPT_CAT_CONVERSION = u"Conversion Options"
OPT_CAT_ENCODING = u"Encoding Options"
OPT_CAT_TEXT = u"Text Options"
OPT_CAT_IMAGE = u"Image Options"
OPT_CAT_REMOVAL = u"Removal Options"
OPT_CAT_SYSTEM = u"System Options"
OPT_CAT_TRANSCODING = u"Transcoding Options"
OPT_CAT_ID3 = u"ID3 Options"
OPT_CAT_REPLAYGAIN = u"ReplayGain Options"
OPT_CAT_BINARIES = u"Binaries Options"

#MetaData Fields
METADATA_TRACK_NAME = u"track name"
METADATA_TRACK_NUMBER = u"track number"
METADATA_TRACK_TOTAL = u"track total"
METADATA_ALBUM_NAME = u"album name"
METADATA_ARTIST_NAME = u"artist name"
METADATA_PERFORMER_NAME = u"performer name"
METADATA_COMPOSER_NAME = u"composer name"
METADATA_CONDUCTOR_NAME = u"conductor name"
METADATA_MEDIA = u"media"
METADATA_ISRC = u"ISRC"
METADATA_CATALOG = u"catalog number"
METADATA_COPYRIGHT = u"copyright"
METADATA_PUBLISHER = u"publisher"
METADATA_YEAR = u"release year"
METADATA_DATE = u"recording date"
METADATA_ALBUM_NUMBER = u"album number"
METADATA_ALBUM_TOTAL = u"album total"
METADATA_COMMENT = u"comment"

#Derived MetaData Fields
METADATA_SUFFIX = u"file name suffix"
METADATA_ALBUM_TRACK_NUMBER = u"combined album and track number"
METADATA_BASENAME = u"file name without suffix"

#ReplayGain
RG_ADDING_REPLAYGAIN = u"Adding ReplayGain"
RG_APPLYING_REPLAYGAIN = u"Applying ReplayGain"
RG_ADDING_REPLAYGAIN_WAIT = \
    u"Adding ReplayGain metadata.  This may take some time."
RG_APPLYING_REPLAYGAIN_WAIT = u"Applying ReplayGain.  This may take some time."
RG_REPLAYGAIN_ADDED = u"ReplayGain added"
RG_REPLAYGAIN_APPLIED = u"ReplayGain applied"

#Labels
LAB_ENCODE = u"%(source)s -> %(destination)s"
LAB_PICTURE = u"Picture"
LAB_T_OPTIONS = u"Please use the -t option to specify %s"
LAB_AVAILABLE_COMPRESSION_TYPES = u"Available quality modes for \"%s\":"
LAB_AVAILABLE_FORMATS = u"Available output formats:"
LAB_OUTPUT_FORMATS = u"Output Formats"
LAB_OUTPUT_TYPE = u"type"
LAB_OUTPUT_QUALITY = u"quality"
LAB_OUTPUT_TYPE_DESCRIPTION = u"name"
LAB_OUTPUT_QUALITY_DESCRIPTION = u"description"
LAB_SUPPORTED_FIELDS = u"Supported fields are:"
LAB_CD2TRACK_PROGRESS = u"track %(track_number)2.2d -> %(filename)s"
LAB_CD2TRACK_LOG = u"Rip log : "
LAB_CD2TRACK_APPLY = u"extract tracks"
LAB_TOTAL_TRACKS = u"Total Tracks"
LAB_TOTAL_LENGTH = u"Total Length"
LAB_TRACK_LENGTH = u"%d:%2.2d"
LAB_TRACK_LENGTH_FRAMES = u"%2d:%2.2d (%d frames)"
LAB_FREEDB_ID = u"FreeDB disc ID"
LAB_MUSICBRAINZ_ID = u"MusicBrainz disc ID"
LAB_CDINFO_LENGTH = u"Length"
LAB_CDINFO_FRAMES = u"Frames"
LAB_CDINFO_OFFSET = u"Offset"
LAB_PLAY_BUTTON = u"play"
LAB_PAUSE_BUTTON = u"pause"
LAB_NEXT_BUTTON = u"next"
LAB_PREVIOUS_BUTTON = u"previous"
LAB_APPLY_BUTTON = u"apply"
LAB_QUIT_BUTTON = u"quit"
LAB_CANCEL_BUTTON = u"cancel"
LAB_BROWSE_BUTTON = u"browse"
LAB_FIELDS_BUTTON = u"fields"
LAB_PLAY_STATUS = u"%(count)d tracks, %(min)d:%(sec)2.2d minutes"
LAB_PLAY_STATUS_1 = u"%(count)d track, %(min)d:%(sec)2.2d minutes"
LAB_PLAY_TRACK = u"track"
LAB_CLOSE = u"close"
LAB_TRACK = u"track"
LAB_X_OF_Y = u"%d / %d"
LAB_TRACK_X_OF_Y = u"track %2.1d / %d"
LAB_CHOOSE_FILE = u"Choose an audio file"
LAB_CHOOSE_DIRECTORY = u"Choose directory"
LAB_ADD_FIELD = u"Add field"
LAB_COVERVIEW_ABOUT = \
    u"A viewer for displaying images embedded in audio files."
LAB_AUDIOTOOLS_URL = u"http://audiotools.sourceforge.net"
LAB_BYTE_SIZE = u"%d bytes"
LAB_DIMENSIONS = u"%d \u00D7 %d"
LAB_BITS_PER_PIXEL = u"%d bits"
LAB_SELECT_BEST_MATCH = u"Select Best Match"
LAB_TRACK_METADATA = u"Track Metadata"
LAB_DVDA_TRACK = u"title %(title_number)d - track %(track_number)2.2d"
LAB_DVDA_TITLE = u"Title %d"
LAB_DVDA_TRACKS = u" (%d tracks)"
LAB_DVDA_TITLE_INFO = \
    u"%(minutes)2.2d:%(seconds)2.2d " + \
    u"%(channels)dch %(rate)s %(bits)d-bit " + \
    u"%(type)s"
LAB_DVDAINFO_TITLE = u"Title"
LAB_DVDAINFO_TRACK = u"Track"
LAB_DVDAINFO_LENGTH = u"Length"
LAB_DVDAINFO_FILENAME = u"Filename"
LAB_DVDAINFO_STARTSECTOR = u"Start Sector"
LAB_DVDAINFO_ENDSECTOR = u"End Sector"
LAB_DVDAINFO_TICKS = u"PTS Ticks"
LAB_DVDA2TRACK_APPLY = u"extract tracks"
LAB_CONVERTING_FILE = u"Converting audio file"
LAB_TRACK2TRACK_APPLY = u"convert tracks"
LAB_TRACK2TRACK_APPLY_1 = u"convert track"
LAB_TRACK2TRACK_NEXT = u"Next Album"
LAB_TRACKCAT_INPUT = u"%d tracks"
LAB_TRACKCAT_APPLY = u"concatenate tracks"
LAB_TRACKCMP_CMP = u"%(file1)s <> %(file2)s"
LAB_TRACKCMP_OK = u"OK"
LAB_TRACKCMP_MISMATCH = u"differ at PCM frame %(frame_number)d"
LAB_TRACKCMP_TYPE_MISMATCH = u"must be either files or directories"
LAB_TRACKCMP_ERROR = u"error"
LAB_TRACKCMP_MISSING = u"\"%(filename)s\" missing from \"%(directory)s\""
LAB_TRACKCMP_RESULTS = u"Results:"
LAB_TRACKCMP_HEADER_SUCCESS = u"success"
LAB_TRACKCMP_HEADER_FAILURE = u"failure"
LAB_TRACKCMP_HEADER_TOTAL = u"total"
LAB_TRACKINFO_BITRATE = u"%(bitrate)4.4s kbps: %(filename)s"
LAB_TRACKINFO_PERCENTAGE = u"%(percentage)3.3s%%: %(filename)s"
LAB_TRACKINFO_ATTRIBS = \
    u"%(minutes)2.2d:%(seconds)2.2d " + \
    u"%(channels)dch %(rate)s %(bits)d-bit: %(filename)s"
LAB_TRACKINFO_REPLAYGAIN = u"ReplayGain:"
LAB_TRACKINFO_TRACK_GAIN = u"track gain"
LAB_TRACKINFO_TRACK_PEAK = u"track peak"
LAB_TRACKINFO_ALBUM_GAIN = u"album gain"
LAB_TRACKINFO_ALBUM_PEAK = u"album peak"
LAB_TRACKINFO_CUESHEET = u"Cuesheet:"
LAB_TRACKINFO_CUESHEET_TRACK = u"track"
LAB_TRACKINFO_CUESHEET_LENGTH = u"length"
LAB_TRACKINFO_CUESHEET_ISRC = u"ISRC"
LAB_TRACKINFO_CHANNELS = u"Assigned Channels:"
LAB_TRACKINFO_CHANNEL = u"channel %(channel_number)d - %(channel_name)s"
LAB_TRACKINFO_UNDEFINED = u"undefined"
LAB_TRACKLENGTH = u"%(hours)d:%(minutes)2.2d:%(seconds)2.2d"
LAB_TRACKLENGTH_FILE_FORMAT = u"format"
LAB_TRACKLENGTH_FILE_COUNT = u"count"
LAB_TRACKLENGTH_FILE_LENGTH = u"length"
LAB_TRACKLENGTH_FILE_SIZE = u"size"
LAB_TRACKLENGTH_FILE_TOTAL = u"total"
LAB_TRACKLINT_RESTORED = u"Restored: %s"
LAB_TRACKLINT_MESSAGE = u"* %(filename)s: %(message)s"
LAB_TRACKRENAME_RENAME = u"rename files"
LAB_TRACKSPLIT_APPLY = u"split track"
LAB_TRACKVERIFY_RESULTS = u"Results:"
LAB_TRACKVERIFY_RESULT_FORMAT = u"format"
LAB_TRACKVERIFY_RESULT_SUCCESS = u"success"
LAB_TRACKVERIFY_RESULT_FAILURE = u"failure"
LAB_TRACKVERIFY_RESULT_TOTAL = u"total"
LAB_TRACKVERIFY_RESULT = u"%(path)s : %(result)s"
LAB_TRACKVERIFY_OK = u"OK"
LAB_TRACKTAG_UPDATING = u"updating tracks"
LAB_TRACKTAG_UPDATED = u"%d tracks updated"
LAB_TRACKTAG_UPDATED_1 = u"1 track updated"
LAB_TRACKTAG_APPLY = u"Apply"
LAB_KEY_NEXT = u" - next %s"
LAB_KEY_PREVIOUS = u" - previous %s"
LAB_KEY_SELECT = u" - select"
LAB_KEY_TOGGLE_OPEN = u" - toggle open"
LAB_KEY_CANCEL = u" - cancel"
LAB_KEY_CLEAR_FORMAT = u" - clear format"
LAB_TRACKTAG_UPDATE_TRACK_NAME = u"the name of the track"
LAB_TRACKTAG_UPDATE_ARTIST_NAME = u"the name of the artist"
LAB_TRACKTAG_UPDATE_PERFORMER_NAME = u"the name of the performer"
LAB_TRACKTAG_UPDATE_COMPOSER_NAME = u"the name of the composer"
LAB_TRACKTAG_UPDATE_CONDUCTOR_NAME = u"the name of the conductor"
LAB_TRACKTAG_UPDATE_ALBUM_NAME = u"the name of the album"
LAB_TRACKTAG_UPDATE_CATALOG = u"the catalog number of the album"
LAB_TRACKTAG_UPDATE_TRACK_NUMBER = u"the number of the track in the album"
LAB_TRACKTAG_UPDATE_TRACK_TOTAL = \
    u"the total number of tracks in the album"
LAB_TRACKTAG_UPDATE_ALBUM_NUMBER = \
    u"the number of the album in a set of albums"
LAB_TRACKTAG_UPDATE_ALBUM_TOTAL = \
    u"the total number of albums in a set of albums"
LAB_TRACKTAG_UPDATE_ISRC = u"the ISRC of the track"
LAB_TRACKTAG_UPDATE_PUBLISHER = u"the publisher of the album"
LAB_TRACKTAG_UPDATE_MEDIA = u"the media type of the album, such as \"CD\""
LAB_TRACKTAG_UPDATE_YEAR = u"the year of release"
LAB_TRACKTAG_UPDATE_DATE = u"the date of recording"
LAB_TRACKTAG_UPDATE_COPYRIGHT = u"copyright information"
LAB_TRACKTAG_UPDATE_COMMENT = u"a text comment"
LAB_TRACKTAG_REMOVE_TRACK_NAME = u"remove track name"
LAB_TRACKTAG_REMOVE_ARTIST_NAME = u"remove track artist"
LAB_TRACKTAG_REMOVE_PERFORMER_NAME = u"remove track performer"
LAB_TRACKTAG_REMOVE_COMPOSER_NAME = u"remove track composer"
LAB_TRACKTAG_REMOVE_CONDUCTOR_NAME = u"remove track conductor"
LAB_TRACKTAG_REMOVE_ALBUM_NAME = u"remove album name"
LAB_TRACKTAG_REMOVE_CATALOG = u"remove catalog number"
LAB_TRACKTAG_REMOVE_TRACK_NUMBER = u"remove track number"
LAB_TRACKTAG_REMOVE_TRACK_TOTAL = u"remove total number of tracks"
LAB_TRACKTAG_REMOVE_ALBUM_NUMBER = u"remove album number"
LAB_TRACKTAG_REMOVE_ALBUM_TOTAL = u"remove total number of albums"
LAB_TRACKTAG_REMOVE_ISRC = u"remove ISRC"
LAB_TRACKTAG_REMOVE_PUBLISHER = u"remove publisher"
LAB_TRACKTAG_REMOVE_MEDIA = u"remove album's media type"
LAB_TRACKTAG_REMOVE_YEAR = u"remove release year"
LAB_TRACKTAG_REMOVE_DATE = u"remove recording date"
LAB_TRACKTAG_REMOVE_COPYRIGHT = u"remove copyright information"
LAB_TRACKTAG_REMOVE_COMMENT = u"remove text comment"
LAB_AT_CONFIG_CD_BURNING = u"CD Burning via track2cd"
LAB_AT_CONFIG_WITHOUT_CUE = u"without cue"
LAB_AT_CONFIG_WITH_CUE = u"with cue"
LAB_AT_CONFIG_YES = u"yes"
LAB_AT_CONFIG_NO = u"no"
LAB_AT_CONFIG_SYS_CONFIG = u"System configuration:"
LAB_AT_CONFIG_USE_MUSICBRAINZ = u"Use MusicBrainz service"
LAB_AT_CONFIG_MUSICBRAINZ_SERVER = u"Default MusicBrainz server"
LAB_AT_CONFIG_MUSICBRAINZ_PORT = u"Default MusicBrainz port"
LAB_AT_CONFIG_USE_FREEDB = u"Use FreeDB service"
LAB_AT_CONFIG_FREEDB_SERVER = u"Default FreeDB server"
LAB_AT_CONFIG_FREEDB_PORT = u"Default FreeDB port"
LAB_AT_CONFIG_DEFAULT_CDROM = u"Default CD-ROM device"
LAB_AT_CONFIG_CDROM_READ_OFFSET = u"CD-ROM sample read offset"
LAB_AT_CONFIG_CDROM_WRITE_OFFSET = u"CD-ROM sample write offset"
LAB_AT_CONFIG_JOBS = u"Default simultaneous jobs"
LAB_AT_CONFIG_VERBOSITY = u"Default verbosity level"
LAB_AT_CONFIG_AUDIO_OUTPUT = u"Audio output"
LAB_AT_CONFIG_FS_ENCODING = u"Filesystem text encoding"
LAB_AT_CONFIG_IO_ENCODING = u"TTY text encoding"
LAB_AT_CONFIG_ID3V2_VERSION = u"ID3v2 tag version"
LAB_AT_CONFIG_ID3V2_ID3V22 = u"ID3v2.2"
LAB_AT_CONFIG_ID3V2_ID3V23 = u"ID3v2.3"
LAB_AT_CONFIG_ID3V2_ID3V24 = u"ID3v2.4"
LAB_AT_CONFIG_ID3V2_NONE = u"no ID3v2 tags"
LAB_AT_CONFIG_ID3V2_PADDING = u"ID3v2 digit padding"
LAB_AT_CONFIG_ID3V2_PADDING_YES = u"padded (\"01\", \"02\", \u2026)"
LAB_AT_CONFIG_ID3V2_PADDING_NO = u"not padded (\"1\", \"2\", \u2026)"
LAB_AT_CONFIG_ID3V1_VERSION = u"ID3v1 tag version"
LAB_AT_CONFIG_ID3V1_ID3V11 = u"ID3v1.1"
LAB_AT_CONFIG_ID3V1_NONE = u"no ID3v1 tags"
LAB_AT_CONFIG_ADD_REPLAY_GAIN = u"Add ReplayGain by default"
LAB_AT_CONFIG_FORMAT = u"File name format : %s"
LAB_AT_CONFIG_FILE_WRITTEN = u"* \"%s\" written"
LAB_AT_CONFIG_FOUND = u"found"
LAB_AT_CONFIG_NOT_FOUND = u"not found"
LAB_AT_CONFIG_TYPE = u" type "
LAB_AT_CONFIG_BINARIES = u"Binaries"
LAB_AT_CONFIG_QUALITY = u" quality "
LAB_AT_CONFIG_REPLAY_GAIN = u" ReplayGain "
LAB_AT_CONFIG_DEFAULT = u"Default"
LAB_AT_CONFIG_TYPE = u"Type"
LAB_AT_CONFIG_DEFAULT_QUALITY = u"Default Quality"
LAB_OUTPUT_OPTIONS = u"Output Options"
LAB_OPTIONS_OUTPUT = u"Output"
LAB_OPTIONS_OUTPUT_DIRECTORY = u"Dir"
LAB_OPTIONS_FILENAME_FORMAT = u"Format"
LAB_OPTIONS_AUDIO_CLASS = u"Type"
LAB_OPTIONS_AUDIO_QUALITY = u"Quality"
LAB_OPTIONS_OUTPUT_FILES = u"Output Files"
LAB_OPTIONS_OUTPUT_FILES_1 = u"Output File"

#Compression settings
COMP_FLAC_0 = u"least compresson, fastest compression speed"
COMP_FLAC_8 = u"most compression, slowest compression speed"
COMP_NERO_LOW = u"lowest quality, corresponds to neroAacEnc -q 0.4"
COMP_NERO_HIGH = u"highest quality, corresponds to neroAacEnc -q 1"
COMP_LAME_0 = u"high quality, larger files, corresponds to lame's -V0"
COMP_LAME_6 = u"lower quality, smaller files, corresponds to lame's -V6"
COMP_LAME_MEDIUM = u"corresponds to lame's --preset medium"
COMP_LAME_STANDARD = u"corresponds to lame's --preset standard"
COMP_LAME_EXTREME = u"corresponds to lame's --preset extreme"
COMP_LAME_INSANE = u"corresponds to lame's --preset insane"
COMP_TWOLAME_64 = u"total bitrate of 64kbps"
COMP_TWOLAME_384 = u"total bitrate of 384kbps"
COMP_VORBIS_0 = u"very low quality, corresponds to oggenc -q 0"
COMP_VORBIS_10 = u"very high quality, corresponds to oggenc -q 10"
COMP_WAVPACK_VERYFAST = u"fastest encode/decode, worst compression"
COMP_WAVPACK_VERYHIGH = u"slowest encode/decode, best compression"

#Errors
ERR_1_FILE_REQUIRED = u"you must specify exactly 1 supported audio file"
ERR_FILES_REQUIRED = u"you must specify at least 1 supported audio file"
ERR_UNSUPPORTED_CHANNEL_MASK = \
    u"unable to write \"%(target_filename)s\" " + \
    u"with channel assignment \"%(assignment)s\""
ERR_UNSUPPORTED_BITS_PER_SAMPLE = \
    u"unable to write \"%(target_filename)s\" " + \
    u"with %(bps)d bits per sample"
ERR_UNSUPPORTED_CHANNEL_COUNT = \
    u"unable to write \"%(target_filename)s\" " + \
    u"with %(channels)d channel input"
ERR_DUPLICATE_FILE = u"file \"%s\" included more than once"
ERR_OUTPUT_IS_INPUT = u"\"%s\" cannot be both input and output file"
ERR_OPEN_IOERROR = u"unable to open \"%s\""
ERR_ENCODING_ERROR = u"unable to write \"%s\""
ERR_UNSUPPORTED_AUDIO_TYPE = u"unsupported audio type \"%s\""
ERR_UNSUPPORTED_FILE = u"unsupported File '%s'"
ERR_INVALID_FILE = u"invalid File '%s'"
ERR_INVALID_SAMPLE_RATE = u"invalid sample rate"
ERR_INVALID_CHANNEL_COUNT = u"invalid channel count"
ERR_INVALID_BITS_PER_SAMPLE = u"invalid bits-per-sample"
ERR_AMBIGUOUS_AUDIO_TYPE = u"ambiguous suffix type \"%s\""
ERR_CHANNEL_COUNT_MASK_MISMATCH = u"channel count and channel mask mismatch"
ERR_NO_PCMREADERS = u"you must have at least 1 PCMReader"
ERR_PICTURES_UNSUPPORTED = u"this MetaData type does not support images"
ERR_UNKNOWN_FIELD = u"unknown field \"%s\" in file format"
ERR_INVALID_FILENAME_FORMAT = u"invalid filename format string"
ERR_FOREIGN_METADATA = u"metadata not from audio file"
ERR_AIFF_NOT_AIFF = u"not an AIFF file"
ERR_AIFF_INVALID_AIFF = u"invalid AIFF file"
ERR_AIFF_INVALID_CHUNK_ID = u"invalid AIFF chunk ID"
ERR_AIFF_INVALID_CHUNK = u"invalid AIFF chunk"
ERR_AIFF_MULTIPLE_COMM_CHUNKS = u"multiple COMM chunks found"
ERR_AIFF_PREMATURE_SSND_CHUNK = u"SSND chunk found before fmt"
ERR_AIFF_MULTIPLE_SSND_CHUNKS = u"multiple SSND chunks found"
ERR_AIFF_TRUNCATED_CHUNK = u"truncated %s chunk found"
ERR_AIFF_NO_COMM_CHUNK = u"COMM chunk not found"
ERR_AIFF_NO_SSND_CHUNK = u"SSND chunk not found"
ERR_AIFF_HEADER_EXTRA_SSND = u"extra data after SSND chunk header"
ERR_AIFF_HEADER_MISSING_SSND = u"missing data in SSND chunk header"
ERR_AIFF_HEADER_IOERROR = u"I/O error reading header data"
ERR_AIFF_FOOTER_IOERROR = u"I/O error reading footer data"
ERR_AIFF_TRUNCATED_SSND_CHUNK = u"premature end of SSND chunk"
ERR_AIFF_INVALID_SIZE = u"total aiff file size mismatch"
ERR_APE_INVALID_HEADER = u"invalid Monkey's Audio header"
ERR_AU_INVALID_HEADER = u"invalid Sun AU header"
ERR_AU_UNSUPPORTED_FORMAT = u"unsupported Sun AU format"
ERR_CUE_INVALID_TOKEN = u"invalid token at char %d"
ERR_CUE_ERROR = u"%(error)s at line %(line)d"
ERR_CUE_INVALID_TRACK_NUMBER = u"invalid track number"
ERR_CUE_INVALID_TRACK_TYPE = u"invalid track type"
ERR_CUE_MISSING_VALUE = u"missing value"
ERR_CUE_EXCESS_DATA = u"excess data"
ERR_CUE_MISSING_FILENAME = u"missing filename"
ERR_CUE_MISSING_FILETYPE = u"missing file type"
ERR_CUE_INVALID_TAG = u"invalid tag %(tag)s at line %(line)d"
ERR_CUE_INVALID_DATA = u"invalid data"
ERR_CUE_INVALID_FLAG = u"invalid flag"
ERR_CUE_INVALID_TIMESTAMP = u"invalid timestamp"
ERR_CUE_INVALID_INDEX_NUMBER = u"invalid index number"
ERR_CUE_MISSING_TAG = u"missing tag at line %d"
ERR_CUE_IOERROR = u"unable to read cuesheet"
ERR_CUE_INVALID_FORMAT = u"cuesheet not formatted for disc images"
ERR_DVDA_IOERROR_AUDIO_TS = u"unable to open AUDIO_TS.IFO"
ERR_DVDA_INVALID_AUDIO_TS = u"invalid AUDIO_TS.IFO"
ERR_DVDA_IOERROR_ATS = u"unable to open ATS_%2.2d_0.IFO"
ERR_DVDA_INVALID_ATS = u"invalid ATS_%2.2d_0.IFO"
ERR_DVDA_INVALID_SECTOR_POINTER = u"invalid sector pointer"
ERR_DVDA_NO_TRACK_SECTOR = u"unable to find track sector in AOB files"
ERR_DVDA_INVALID_AOB_SYNC = u"invalid AOB sync bytes"
ERR_DVDA_INVALID_AOB_MARKER = u"invalid AOB marker bits"
ERR_DVDA_INVALID_AOB_START = u"invalid AOB packet start code"
ERR_FLAC_RESERVED_BLOCK = u"reserved metadata block type %d"
ERR_FLAC_INVALID_BLOCK = u"invalid metadata block type"
ERR_FLAC_INVALID_FILE = u"Invalid FLAC file"
ERR_OGG_INVALID_MAGIC_NUMBER = u"invalid Ogg magic number"
ERR_OGG_INVALID_VERSION = u"invalid Ogg version"
ERR_OGG_CHECKSUM_MISMATCH = u"Ogg page checksum mismatch"
ERR_OGGFLAC_INVALID_PACKET_BYTE = u"invalid packet byte"
ERR_OGGFLAC_INVALID_OGG_SIGNATURE = u"invalid Ogg signature"
ERR_OGGFLAC_INVALID_MAJOR_VERSION = u"invalid major version"
ERR_OGGFLAC_INVALID_MINOR_VERSION = u"invalid minor version"
ERR_OGGFLAC_VALID_FLAC_SIGNATURE = u"invalid FLAC signature"
ERR_IMAGE_UNKNOWN_TYPE = u"unknown image type"
ERR_IMAGE_INVALID_JPEG_MARKER = u"invalid JPEG segment marker"
ERR_IMAGE_IOERROR_JPEG = "I/O error reading JPEG data"
ERR_IMAGE_INVALID_PNG = u"invalid PNG"
ERR_IMAGE_IOERROR_PNG = "I/O error reading PNG data"
ERR_IMAGE_INVALID_PLTE = u"invalid PLTE chunk length"
ERR_IMAGE_INVALID_BMP = u"invalid BMP"
ERR_IMAGE_IOERROR_BMP = "I/O error reading BMP data"
ERR_IMAGE_INVALID_TIFF = u"invalid TIFF"
ERR_IMAGE_IOERROR_TIFF = u"I/O error reading TIFF data"
ERR_IMAGE_INVALID_GIF = u"invalid GIF"
ERR_IMAGE_IOERROR_GIF = u"I/O error reading GIF data"
ERR_M4A_IOERROR = u"I/O error opening M4A file"
ERR_M4A_MISSING_MDIA = u"required mdia atom not found"
ERR_M4A_MISSING_STSD = u"required stsd atom not found"
ERR_M4A_INVALID_MP4A = u"invalid mp4a atom"
ERR_M4A_MISSING_MDHD = u"required mdhd atom not found"
ERR_M4A_UNSUPPORTED_MDHD = u"unsupported mdhd version"
ERR_M4A_INVALID_MDHD = u"invalid mdhd atom"
ERR_M4A_INVALID_LEAF_ATOMS = u"leaf atoms must be a list"
ERR_ALAC_IOERROR = u"I/O error opening ALAC file"
ERR_ALAC_INVALID_ALAC = u"invalid alac atom"
ERR_MP3_FRAME_NOT_FOUND = u"MP3 frame not found"
ERR_MP3_INVALID_SAMPLE_RATE = u"invalid sample rate"
ERR_MP3_INVALID_BIT_RATE = u"invalid bit rate"
ERR_TOC_NO_HEADER = u"no CD_DA TOC header found"
ERR_VORBIS_INVALID_TYPE = u"invalid Vorbis type"
ERR_VORBIS_INVALID_HEADER = u"invalid Vorbis header"
ERR_VORBIS_INVALID_VERSION = u"invalid Vorbis version"
ERR_VORBIS_INVALID_FRAMING_BIT = u"invalid framing bit"
ERR_OPUS_INVALID_TYPE = u"invalid Opus header"
ERR_OPUS_INVALID_VERSION = u"invalid Opus version"
ERR_OPUS_INVALID_CHANNELS = u"invalid Open channel count"
ERR_WAV_NOT_WAVE = u"not a RIFF WAVE file"
ERR_WAV_INVALID_WAVE = u"invalid RIFF WAVE file"
ERR_WAV_NO_DATA_CHUNK = u"data chunk not found"
ERR_WAV_INVALID_CHUNK = u"invalid RIFF WAVE chunk ID"
ERR_WAV_MULTIPLE_FMT = u"multiple fmt chunks found"
ERR_WAV_PREMATURE_DATA = u"data chunk found before fmt"
ERR_WAV_MULTIPLE_DATA = u"multiple data chunks found"
ERR_WAV_TRUNCATED_CHUNK = u"truncated %s chunk found"
ERR_WAV_NO_FMT_CHUNK = u"fmt chunk not found"
ERR_WAV_HEADER_EXTRA_DATA = u"%d bytes found after data chunk header"
ERR_WAV_HEADER_IOERROR = u"I/O error reading header data"
ERR_WAV_FOOTER_IOERROR = u"I/O error reading footer data"
ERR_WAV_TRUNCATED_DATA_CHUNK = u"premature end of data chunk"
ERR_WAV_INVALID_SIZE = u"total wave file size mismatch"
ERR_WAVPACK_INVALID_HEADER = u"WavPack header ID invalid"
ERR_WAVPACK_UNSUPPORTED_FMT = u"unsupported FMT compression"
ERR_WAVPACK_INVALID_FMT = u"invalid FMT chunk"
ERR_WAVPACK_NO_FMT = u"FMT chunk not found in WavPack"
ERR_NO_COMPRESSION_MODES = u"Audio type \"%s\" has no quality modes"
ERR_UNSUPPORTED_COMPRESSION_MODE = \
    u"\"%(quality)s\" is not a supported compression mode " + \
    u"for type \"%(type)s\""
ERR_INVALID_CDDA = u". Is that an audio cd?"
ERR_NO_CDDA = u"no CD in drive"
ERR_NO_EMPTY_CDDA = u"no audio tracks found on CD"
ERR_NO_OUTPUT_FILE = u"you must specify an output file"
ERR_DUPLICATE_OUTPUT_FILE = u"output file \"%s\" occurs more than once"
ERR_URWID_REQUIRED = u"Urwid 1.0 or better is required for interactive mode"
ERR_GET_URWID1 = \
    u"Please download and install urwid from http://excess.org/urwid/"
ERR_GET_URWID2 = u"or your system's package manager."
ERR_TERMIOS_ERROR = u"unable to get tty settings"
ERR_TERMIOS_SUGGESTION = \
    u"if piping arguments via xargs(1), try:"
ERR_NO_GUI = u"neither PyGTK nor Tkinter is available"
ERR_NO_AUDIO_TS = \
    u"you must specify the DVD-Audio's AUDIO_TS directory with -A"
ERR_INVALID_TITLE_NUMBER = u"title number must be greater than 0"
ERR_INVALID_JOINT = u"you must run at least 1 process at a time"
ERR_NO_CDRDAO = u"unable to find \"cdrdao\" executable"
ERR_GET_CDRDAO = u"please install \"cdrdao\" to burn CDs"
ERR_NO_CDRECORD = u"unable to find \"cdrecord\" executable"
ERR_GET_CDRECORD = u"please install \"cdrecord\" to burn CDs"
ERR_SAMPLE_RATE_MISMATCH = u"all audio files must have the same sample rate"
ERR_CHANNEL_COUNT_MISMATCH = \
    u"all audio files must have the same channel count"
ERR_CHANNEL_MASK_MISMATCH = \
    u"all audio files must have the same channel assignment"
ERR_BPS_MISMATCH = u"all audio files must have the same bits per sample"
ERR_TRACK2CD_INVALIDFILE = u"not all files are valid.  Unable to write CD"
ERR_TRACK2TRACK_O_AND_D = u"-o and -d options are not compatible"
ERR_TRACK2TRACK_O_AND_D_SUGGESTION = \
    u"please specify either -o or -d but not both"
ERR_TRACK2TRACK_O_AND_FORMAT = u"--format has no effect when used with -o"
ERR_TRACK2TRACK_O_AND_MULTIPLE = \
    u"you may specify only 1 input file for use with -o"
ERR_TRACKCMP_TYPE_MISMATCH = u"both files to be compared must be audio files"
ERR_TRACKSPLIT_NO_CUESHEET = u"you must specify a cuesheet to split audio file"
ERR_TRACKSPLIT_OVERLONG_CUESHEET = u"cuesheet too long for track being split"
ERR_NO_UNDO_DB = u"cannot perform undo without undo db"
ERR_RENAME = u"unable to rename \"%(source)s\" to \"%(target)s\""
ERR_INVALID_IMAGE = u"%(filename)s: %(message)s"
ERR_TRACKTAG_COMMENT_NOT_UTF8 = \
    u"comment file \"%s\" does not appear to be UTF-8 text"
ERR_TRACKTAG_COMMENT_IOERROR = u"unable to open comment file \"%s\""
ERR_OUTPUT_DUPLICATE_NAME = u"all output tracks must have different names"
ERR_OUTPUT_OUTPUTS_ARE_INPUT = \
    u"output tracks must have different names than input tracks"
ERR_OUTPUT_INVALID_FORMAT = u"output tracks must have valid format string"

#Cleaning messages
CLEAN_REMOVE_DUPLICATE_TAG = u"removed duplicate tag %(field)s"
CLEAN_REMOVE_TRAILING_WHITESPACE = \
    u"removed trailing whitespace from %(field)s"
CLEAN_REMOVE_LEADING_WHITESPACE = u"removed leading whitespace from %(field)s"
CLEAN_REMOVE_LEADING_WHITESPACE_ZEROES = \
    u"removed leading whitespace/zeroes from %(field)s"
CLEAN_REMOVE_LEADING_ZEROES = u"removed leading zeroes from %(field)s"
CLEAN_ADD_LEADING_ZEROES = u"added leading zeroes to %(field)s"
CLEAN_REMOVE_EMPTY_TAG = u"removed empty field %(field)s"
CLEAN_FIX_TAG_FORMATTING = u"fixed formatting for %(field)s"
CLEAN_FIX_IMAGE_FIELDS = u"fixed embedded image metadata fields"
CLEAN_AIFF_MULTIPLE_COMM_CHUNKS = u"removed duplicate COMM chunk"
CLEAN_AIFF_REORDERED_SSND_CHUNK = u"moved COMM chunk after SSND chunk"
CLEAN_AIFF_MULTIPLE_SSND_CHUNKS = u"removed duplicate SSND chunk"
CLEAN_FLAC_REORDERED_STREAMINFO = u"moved STREAMINFO to first block"
CLEAN_FLAC_MULITPLE_STREAMINFO = u"removed redundant STREAMINFO block"
CLEAN_FLAC_MULTIPLE_VORBISCOMMENT = u"removed redundant VORBIS_COMMENT block"
CLEAN_FLAC_MULTIPLE_SEEKTABLE = u"removed redundant SEEKTABLE block"
CLEAN_FLAC_MULTIPLE_CUESHEET = u"removed redundant CUESHEET block"
CLEAN_FLAC_UNDEFINED_BLOCK = u"removed undefined block"
CLEAN_FLAC_REMOVE_SEEKPOINTS = u"removed empty seekpoints from seektable"
CLEAN_FLAC_REORDER_SEEKPOINTS = u"reordered seektable to be in ascending order"
CLEAN_FLAC_REMOVE_ID3V2 = u"removed ID3v2 tag"
CLEAN_FLAC_REMOVE_ID3V1 = u"removed ID3v1 tag"
CLEAN_FLAC_POPULATE_MD5 = u"populated empty MD5SUM"
CLEAN_FLAC_ADD_CHANNELMASK = u"added WAVEFORMATEXTENSIBLE_CHANNEL_MASK"
CLEAN_FLAC_FIX_SEEKTABLE = u"fixed invalid SEEKTABLE"
CLEAN_WAV_MULTIPLE_FMT_CHUNKS = u"removed duplicate fmt chunk"
CLEAN_WAV_REORDERED_DATA_CHUNK = u"moved data chunk after fmt chunk"
CLEAN_WAV_MULTIPLE_DATA_CHUNKS = u"removed multiple data chunk"

#Channel names
MASK_FRONT_LEFT = u"front left"
MASK_FRONT_RIGHT = u"front right"
MASK_FRONT_CENTER = u"front center"
MASK_LFE = u"low frequency"
MASK_BACK_LEFT = u"back left"
MASK_BACK_RIGHT = u"back right"
MASK_FRONT_RIGHT_OF_CENTER = u"front right of center"
MASK_FRONT_LEFT_OF_CENTER = u"front left of center"
MASK_BACK_CENTER = u"back center"
MASK_SIDE_LEFT = u"side left"
MASK_SIDE_RIGHT = u"side right"
MASK_TOP_CENTER = u"top center"
MASK_TOP_FRONT_LEFT = u"top front left"
MASK_TOP_FRONT_CENTER = u"top front center"
MASK_TOP_FRONT_RIGHT = u"top front right"
MASK_TOP_BACK_LEFT = u"top back left"
MASK_TOP_BACK_CENTER = u"top back center"
MASK_TOP_BACK_RIGHT = u"top back right"
