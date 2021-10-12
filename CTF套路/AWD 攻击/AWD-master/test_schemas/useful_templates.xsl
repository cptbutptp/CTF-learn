<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
    xmlns:eg="http://www.tei-c.org/ns/Examples"
    xmlns:tei="http://www.tei-c.org/ns/1.0" 
    xmlns:xd="http://www.oxygenxml.com/ns/doc/xsl"
    xmlns:exsl="http://exslt.org/common"
    xmlns:msxsl="urn:schemas-microsoft-com:xslt"
    xmlns:fn="http://www.w3.org/2005/xpath-functions"
    extension-element-prefixes="exsl msxsl"
    xmlns="http://www.w3.org/1999/xhtml" 
    xmlns:html="http://www.w3.org/1999/xhtml" 
    exclude-result-prefixes="xsl tei xd eg fn #default">
    <xd:desc>
        <xd:p><xd:b>Created on:</xd:b> Nov 17, 2011</xd:p>
        <xd:p><xd:b>Author:</xd:b> John A. Walsh</xd:p>
        <xd:p>TEI Boilerplate stylesheet: Copies TEI document, with a very few modifications
            into an html shell, which provides access to javascript and other features from the
            html/browser environment.</xd:p>
    </xd:desc>
    
   <!--these are higher-order templates for setting up the HTML shell-->
    
    <xd:doc xmlns:xd="http://www.oxygenxml.com/ns/doc/xsl">
        <xd:desc>
            <xd:p>Match document root and create and html5 wrapper for the TEI document, which is
                copied, with some modification, into the HTML document.</xd:p>
        </xd:desc>
    </xd:doc>
    
    <xsl:key name="ids" match="//*" use="@xml:id"/>
    
    <xsl:template match="/" name="htmlShell" priority="99">
        <html>
            <xsl:call-template name="htmlHead"/>
            <body>
                <xsl:if test="$includeToolbox = true()">
                    <xsl:call-template name="teibpToolbox"/>
                </xsl:if>
                <div id="tei_wrapper">
                    <xsl:apply-templates/>
                </div>
                <xsl:copy-of select="$htmlFooter"/>
                <script type="text/javascript" src="{$teibpJS}"></script>
            </body>
        </html>
    </xsl:template>
    
    <xd:doc>
        <xd:desc>
            <xd:p>Basic copy template, copies all attribute nodes from source XML tree to output
                document.</xd:p>
        </xd:desc>
    </xd:doc>
    <xsl:template match="@*">
        <xsl:copy/>
    </xsl:template>
    
    <xd:doc>
        <xd:desc>
            <xd:p>Template for elements, which handles style and adds an @xml:id to every element.
                Existing @xml:id attributes are retained unchanged.</xd:p>
        </xd:desc>
    </xd:doc>
    <xsl:template match="*" name="teibp-default">
        <xsl:element name="{local-name()}">
            <xsl:apply-templates select="@*"/>
            <xsl:call-template name="addID"/>
            <xsl:call-template name="rendition"/>
            <xsl:apply-templates select="node()"/>
        </xsl:element>
    </xsl:template>
    
    
    <!--templates for inline CSS-->
    
    <xd:doc xmlns:xd="http://www.oxygenxml.com/ns/doc/xsl">
        <xd:desc>
            <xd:p>Template moves value of @rend into an html @style attribute. Stylesheet assumes
                CSS is used in @rend to describe renditions, i.e., styles.</xd:p>
        </xd:desc>
    </xd:doc>
    <xsl:template match="@rend">
        <xsl:choose>
            <xsl:when test="$inlineCSS = true()">
                <xsl:attribute name="style">
                    <xsl:value-of select="."/>
                </xsl:attribute>
            </xsl:when>
            <xsl:otherwise>
                <xsl:copy>
                    <xsl:apply-templates select="@*|node()"/>
                </xsl:copy>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
    
    <xsl:template name="rendition">
        <xsl:if test="@rendition">
            <xsl:attribute name="rendition">
                <xsl:value-of select="@rendition"/>
            </xsl:attribute>
        </xsl:if>
    </xsl:template>
    
    <!--templates for linking-->
    
    <xsl:template match="@xml:id">
        <!-- @xml:id is copied to @id, which browsers can use
			for internal links.
		-->
        <!--
		<xsl:attribute name="xml:id">
			<xsl:value-of select="."/>
		</xsl:attribute>
		-->
        <xsl:attribute name="id">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xd:doc>
        <xd:desc>
            <xd:p>Transforms TEI ref element to html a (link) element.</xd:p>
        </xd:desc>
    </xd:doc>
    <xsl:template match="tei:ref[@target]" priority="99">
        <a href="{@target}">
            <xsl:apply-templates select="@*"/>
            <xsl:call-template name="rendition"/>
            <xsl:apply-templates select="node()"/>
        </a>
    </xsl:template>
    
    <xd:doc>
        <xd:desc>
            <xd:p>Transforms TEI ptr element to html a (link) element.</xd:p>
        </xd:desc>
    </xd:doc>
    <xsl:template match="tei:ptr[@target]" priority="99">
        <a href="{@target}">
            <xsl:apply-templates select="@*"/>
            <xsl:call-template name="rendition"/>
            <xsl:value-of select="normalize-space(@target)"/>
        </a>
    </xsl:template>
    
    <!--templates for images-->
    
    <xd:doc>
        <xd:desc>
            <xd:p>Transforms TEI figure element to html img element.</xd:p>
        </xd:desc>
    </xd:doc>
    <xsl:template match="tei:figure[tei:graphic[@url]]" priority="99">
        <xsl:copy>
            <xsl:apply-templates select="@*"/>
            <xsl:call-template name="addID"/>
            <figure>
                <img alt="{normalize-space(tei:figDesc)}" src="{tei:graphic/@url}"/>
                <xsl:apply-templates select="*[ not( self::tei:graphic | self::tei:figDesc ) ]"/>
            </figure>
        </xsl:copy>
    </xsl:template>
    
    
    
    
    
</xsl:stylesheet>